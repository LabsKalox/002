import subprocess,numpy as np,sys
from PIL import Image
W,H=270,480
def frames(f,ss,t,fps=None):
    vf=f"scale={W}:{H},format=gray"
    b=subprocess.run(["ffmpeg","-v","error","-ss",str(ss),"-t",str(t),"-i",f,"-vf",vf,"-f","rawvideo","-"],capture_output=True).stdout
    return np.frombuffer(b,np.uint8).reshape(-1,H,W)
src=sys.argv[1]; final=sys.argv[2]; trim=float(sys.argv[3]); clipstart=float(sys.argv[4]); T0=float(sys.argv[5]); T1=float(sys.argv[6])
scale_fn=eval(sys.argv[7])  # lambda film_t -> scale
S=frames(src,0,8)   # 24 fps source, all frames
F=frames(final,T0-trim,T1-T0)
oy=0.38*H; ox=W/2
def scaled(img,s):
    im=Image.fromarray(img)
    # output pixel (x,y) samples input ((x-ox)/s+ox,(y-oy)/s+oy)
    a=1/s; c=ox-ox*a; e=oy-oy*a
    return np.asarray(im.transform((W,H),Image.AFFINE,(a,0,c,0,a,e),resample=Image.BILINEAR)).astype(np.float32)
offs=[]
for i,fr in enumerate(F):
    T=T0+i/30.0; m=T-clipstart; exp=m*24
    s=scale_fn(T); best=None
    for j in range(int(exp)-4,int(exp)+5):
        if 0<=j<len(S):
            e=np.mean((scaled(S[j],s)-fr.astype(np.float32))**2)
            if best is None or e<best[0]: best=(e,j)
    offs.append(best[1]-exp)
offs=np.array(offs)
print("frames",len(offs),"picture offset vs expected (source frames @24fps, + = ahead, - = behind):")
print(" mean %.2f  min %.2f  max %.2f"%(offs.mean(),offs.min(),offs.max()))
print(" in ms: mean %+.0f  min %+.0f  max %+.0f"%(offs.mean()/24*1000,offs.min()/24*1000,offs.max()/24*1000))
print(" ".join("%+.1f"%o for o in offs[:60]))
