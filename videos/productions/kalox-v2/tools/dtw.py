import subprocess, numpy as np, json
SR=16000; HOP=160; NFFT=512
def load(p, ss, t):
    b=subprocess.run(["ffmpeg","-v","error","-ss",str(ss),"-t",str(t),"-i",p,"-ac","1","-ar",str(SR),"-f","s16le","-"],capture_output=True,check=True).stdout
    return np.frombuffer(b,np.int16).astype(np.float32)/32768
def mel_fb(n=40):
    hz=lambda m:700*(10**(m/2595)-1); mel=lambda f:2595*np.log10(1+f/700)
    pts=hz(np.linspace(mel(60),mel(7600),n+2)); bins=np.floor((NFFT+1)*pts/SR).astype(int)
    fb=np.zeros((n,NFFT//2+1))
    for i in range(1,n+1):
        l,c,r=bins[i-1],bins[i],bins[i+1]
        fb[i-1,l:c]=(np.arange(l,c)-l)/max(c-l,1); fb[i-1,c:r]=(r-np.arange(c,r))/max(r-c,1)
    return fb
FB=mel_fb()
N=40; K=np.arange(13)[:,None]; D=np.cos(np.pi*K*(np.arange(N)+0.5)/N)
def mfcc(y):
    w=np.hanning(NFFT); fr=[y[i:i+NFFT]*w for i in range(0,len(y)-NFFT,HOP)]
    S=np.abs(np.fft.rfft(np.array(fr),axis=1))**2
    m=np.log(S@FB.T+1e-8); c=(D@m.T).T[:,1:]
    c=(c-c.mean(0))/(c.std(0)+1e-8)
    return c
V="/home/user/002/videos/"
# film time t  <->  user source time t+0.68 ; veo time = veo clip time
u0,u1=0.20,6.00          # film window of user speech
v0,v1=0.15,6.75          # veo speech window
U=mfcc(load(V+"references/kalox/source.mp4",u0+0.68,u1-u0))
W=mfcc(load(V+"assets/raw/aroll-preto-B.mp4",v0,v1-v0))
C=((U[:,None,:]-W[None,:,:])**2).sum(-1)**0.5
n,m=C.shape; A=np.full((n+1,m+1),np.inf); A[0,0]=0
for i in range(1,n+1):
    ci=C[i-1]; prev=A[i-1]
    row=np.empty(m+1); row[0]=np.inf
    diag=prev[:-1]; up=prev[1:]
    best=np.minimum(diag,up)+ci  # without left move
    for j in range(1,m+1):
        b=best[j-1]; l=row[j-1]+ci[j-1]
        row[j]=b if b<l else l
    A[i]=row
i,j=n,m; path=[(i-1,j-1)]
while i>1 or j>1:
    opts=[(A[i-1,j-1],i-1,j-1),(A[i-1,j],i-1,j),(A[i,j-1],i,j-1)]
    _,i,j=min(opts); path.append((i-1,j-1))
path=path[::-1]
# film frame (30 fps) -> veo time
fmap={}
for a,b in path:
    ft=u0+a*HOP/SR; vt=v0+b*HOP/SR; fmap.setdefault(round(ft*30),[]).append(vt)
pts=sorted((f,float(np.median(v))) for f,v in fmap.items())
json.dump(pts,open("/tmp/claude-0/-home-user-002/87f6385b-7dc3-5fa8-9d19-914098da7b2e/scratchpad/dtw_map.json","w"))
for f,v in pts[::6]: print(f"film {f:4d}f ({f/30:5.2f}s)  veo {v:5.2f}s  delta {v-f/30:+.2f}")
