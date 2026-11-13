import subprocess, numpy as np, sys
def env(p):
    b=subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
    y=np.frombuffer(b,np.int16).astype(np.float32)/32768; h=160
    return np.array([np.sqrt(np.mean(y[i:i+h]**2)) for i in range(0,len(y)-h,h)])
g=env(sys.argv[1]); u=env(sys.argv[2])
gd=20*np.log10(g+1e-4); ud=20*np.log10(u+1e-4)
a,b=float(sys.argv[3]),float(sys.argv[4])
for i in range(int(a*100),int(b*100),4):
    print("%6.2f  guide %s  voice %s"%(i/100, ("#"*max(0,int((gd[i]+60)/2))).ljust(30), "#"*max(0,int((ud[i]+60)/2))))
