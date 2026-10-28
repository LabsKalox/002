# Lip-sync helper: aligns the new voice to each Veo clip's own (lip-synced) voice with MFCC+DTW,
# then renders a retimed, silent copy of the clip whose mouth follows the new voice.
# usage: tools-sync.py <voice> <voice_from> <voice_to> <clip> <ref_ranges "a-b,c-d"> <out.mp4> <tail_extra_s>
import subprocess, numpy as np, sys, json
import os
SR=16000; HOP=160; NFFT=512; MAXRATE=float(os.environ.get("MAXRATE","1.8"))
def load(p, ss=None, t=None):
    cmd=["ffmpeg","-v","error"]+(["-ss",str(ss)] if ss is not None else [])+(["-t",str(t)] if t is not None else [])+["-i",p,"-ac","1","-ar",str(SR),"-f","s16le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True,check=True).stdout,np.int16).astype(np.float32)/32768
def mel_fb(n=40):
    hz=lambda m:700*(10**(m/2595)-1); mel=lambda f:2595*np.log10(1+f/700)
    pts=hz(np.linspace(mel(60),mel(7600),n+2)); bins=np.floor((NFFT+1)*pts/SR).astype(int); fb=np.zeros((n,NFFT//2+1))
    for i in range(1,n+1):
        l,c,r=bins[i-1],bins[i],bins[i+1]
        fb[i-1,l:c]=(np.arange(l,c)-l)/max(c-l,1); fb[i-1,c:r]=(r-np.arange(c,r))/max(r-c,1)
    return fb
FB=mel_fb(); K=np.arange(13)[:,None]; D=np.cos(np.pi*K*(np.arange(40)+0.5)/40)
def mfcc(y):
    w=np.hanning(NFFT); fr=np.array([y[i:i+NFFT]*w for i in range(0,len(y)-NFFT,HOP)])
    m=np.log((np.abs(np.fft.rfft(fr,axis=1))**2)@FB.T+1e-8); c=(D@m.T).T[:,1:]
    return (c-c.mean(0))/(c.std(0)+1e-8)
def dtw(U,W):
    C=np.sqrt(((U[:,None,:]-W[None,:,:])**2).sum(-1)); n,m=C.shape; A=np.full((n+1,m+1),np.inf); A[0,0]=0
    for i in range(1,n+1):
        ci=C[i-1]; prev=A[i-1]; best=np.minimum(prev[:-1],prev[1:])+ci; row=np.empty(m+1); row[0]=np.inf
        for j in range(1,m+1):
            l=row[j-1]+ci[j-1]; row[j]=best[j-1] if best[j-1]<l else l
        A[i]=row
    i,j=n,m; path=[(i-1,j-1)]
    while i>1 or j>1:
        _,i,j=min((A[i-1,j-1],i-1,j-1),(A[i-1,j],i-1,j),(A[i,j-1],i,j-1)); path.append((i-1,j-1))
    return path[::-1]
voice,v0,v1,clip,ranges,out,tail=sys.argv[1],float(sys.argv[2]),float(sys.argv[3]),sys.argv[4],sys.argv[5],sys.argv[6],float(sys.argv[7])
rngs=[tuple(map(float,r.split("-"))) for r in ranges.split(",")]
U=mfcc(load(voice,v0,v1-v0))
ref=np.concatenate([load(clip,a,b-a) for a,b in rngs]); W=mfcc(ref)
def ref_to_src(t):  # time inside the concatenated reference -> source clip time
    acc=0.0
    for a,b in rngs:
        if t<=acc+(b-a): return a+(t-acc)
        acc+=b-a
    return rngs[-1][1]
path=dtw(U,W)
fmap={}
for a,b in path: fmap.setdefault(round(a*HOP/SR*30),[]).append(ref_to_src(b*HOP/SR))
f=np.array(sorted(fmap)); s=np.maximum.accumulate(np.array([np.median(fmap[k]) for k in f]))
L=round((v1-v0)*30)
# pieces of 6 frames; a jump bigger than 0.35 s inside a piece becomes a hard cut
pieces=[]; fr=0
while fr<L:
    nx=min(fr+6,L); s0=float(np.interp(fr,f,s)); s1=float(np.interp(nx,f,s))
    dur=(nx-fr)/30
    if (s1-s0)/dur>MAXRATE: s0=s1-dur      # Veo pause much longer than the voice: hard cut instead of fast-forward
    if (s1-s0)/dur<0.5: s1=s0+0.5*dur      # never slower than half speed
    pieces.append((fr,nx,s0,s1)); fr=nx
if tail>0:
    s_end=pieces[-1][3]; pieces.append((L,L+round(tail*30),s_end,s_end+tail))
# optional 8th arg "OFFSET:HOLD_UNTIL:ZERO_AT" shifts the mouth by OFFSET seconds at the start of the block,
# held until HOLD_UNTIL and ramped back to 0 at ZERO_AT (fixes a residual lead measured after the DTW).
if len(sys.argv)>8:
    off,hold,zero=map(float,sys.argv[8].split(":"))
    def shift(t):
        return off if t<=hold else (off*(zero-t)/(zero-hold) if t<zero else 0.0)
    pieces=[(t0,t1,max(0.0,s0+shift(t0/30)),max(1/30,s1+shift(t1/30))) for t0,t1,s0,s1 in pieces]
json.dump([list(p) for p in pieces],open(out+".pieces.json","w"))
fc=[]; labels=[]
for k,(t0,t1,s0,s1) in enumerate(pieces):
    dur=(t1-t0)/30; rate=(s1-s0)/dur
    fc.append(f"[0:v]trim=start={s0:.4f}:end={s1:.4f},setpts=(PTS-STARTPTS)/{rate:.5f},fps=30,trim=end_frame={t1-t0},setpts=PTS-STARTPTS[p{k}]"); labels.append(f"[p{k}]")
fc.append("".join(labels)+f"concat=n={len(labels)}:v=1:a=0[v]")
subprocess.run(["ffmpeg","-v","error","-y","-i",clip,"-filter_complex",";".join(fc),"-map","[v]","-r","30","-c:v","libx264","-crf","16","-preset","medium","-pix_fmt","yuv420p","-an",out],check=True)
rates=[(p[3]-p[2])/((p[1]-p[0])/30) for p in pieces]
cutlist=[(round(pieces[i][0]/30,2),round(pieces[i][2]-pieces[i-1][3],2)) for i in range(1,len(pieces)) if abs(pieces[i][2]-pieces[i-1][3])>0.05]; cuts=cutlist
print(json.dumps({"cuts":cuts,"out":out,"frames":pieces[-1][1],"rate_min":round(min(rates),2),"rate_max":round(max(rates),2),"src_start":round(pieces[0][2],2),"src_end":round(pieces[-1][3],2)}))
