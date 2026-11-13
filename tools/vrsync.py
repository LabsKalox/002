import subprocess, numpy as np, sys
def env(p):
    b=subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
    y=np.frombuffer(b,np.int16).astype(np.float32)/32768; h=160
    return np.array([np.sqrt(np.mean(y[i:i+h]**2)) for i in range(0,len(y)-h,h)])
g=env(sys.argv[1]); u=env(sys.argv[2])
def lag(a,b,R):
    a=(a-a.mean())/(a.std()+1e-9); b=(b-b.mean())/(b.std()+1e-9); best=(-9,0)
    for L in range(-R,R+1):
        n=min(len(a),len(b)-L) if L>=0 else min(len(a)+L,len(b))
        x=a[max(0,-L):max(0,-L)+n]; y=b[max(0,L):max(0,L)+n]
        if n>50: best=max(best,(float(np.mean(x*y)),L))
    return best
c,L=lag(g,u,60); print("global: voice = guide %+d ms (corr %.2f)"%(L*10,c))
for w in np.arange(0.0,min(len(g),len(u))/100-0.6,0.6):
    a=g[int(w*100):int(w*100)+60]
    if a.std()<2e-3: continue
    seg=u[max(0,int(w*100)+L-30):int(w*100)+L+90]
    best=(-9,0)
    an=(a-a.mean())/(a.std()+1e-9)
    for k in range(0,len(seg)-60+1):
        b=seg[k:k+60]; bn=(b-b.mean())/(b.std()+1e-9); best=max(best,(float(np.mean(an*bn)),k))
    off=best[1]-min(30,int(w*100)+L)+L
    print("%5.1f s  %+4d ms  corr %.2f"%(w,off*10,best[0]))
def onsets(e):
    db=20*np.log10(e+1e-4); on=db>db.max()-30; out=[];s=None
    for i,v in enumerate(on):
        if v and s is None: s=i
        if not v and s is not None:
            if i-s>8: out.append((s/100,i/100))
            s=None
    return out
print("guide speech:", onsets(g)[:3], "...", onsets(g)[-2:])
print("voice speech:", onsets(u)[:3], "...", onsets(u)[-2:])
