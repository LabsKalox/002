# Bateria house 120 bpm (kick, hats, clap, conga) SEM baixo: o baixo do vídeo é só o do BassForge.
import numpy as np, wave, sys
SR=48000; BPM=120; beat=60/BPM; dur=float(sys.argv[2]) if len(sys.argv)>2 else 20.0
N=int(SR*dur); out=np.zeros(N); rng=np.random.default_rng(7)
def add(sig,t,g=1.0):
    i=int(round(t*SR)); j=min(N,i+len(sig))
    if 0<=i<N: out[i:j]+=g*sig[:j-i]
def kick():
    t=np.arange(int(SR*0.35))/SR; f=50*(1+3*np.exp(-t*35)); ph=2*np.pi*np.cumsum(f)/SR
    return np.tanh(2.2*np.sin(ph))*np.exp(-t*9)
def clap():
    t=np.arange(int(SR*0.22))/SR; n=rng.standard_normal(len(t))
    a=np.convolve(n,np.ones(3)/3,'same')-np.convolve(n,np.ones(20)/20,'same')
    return a*(np.exp(-t*30)+0.5*np.exp(-np.maximum(t-0.01,0)*35)*(t>0.01))*0.8
def hat(open_=False):
    t=np.arange(int(SR*(0.16 if open_ else 0.04)))/SR; n=rng.standard_normal(len(t))
    return (n-np.convolve(n,np.ones(4)/4,'same'))*np.exp(-t*(16 if open_ else 80))*0.3
def conga(f=220):
    t=np.arange(int(SR*0.18))/SR; fr=f*(1+0.4*np.exp(-t*60)); ph=2*np.pi*np.cumsum(fr)/SR
    return np.sin(ph)*np.exp(-t*22)*0.5
bar=4*beat; t=0.0
while t<dur:
    for q in range(4):
        add(kick(),t+q*beat,0.95); add(hat(open_=True),t+q*beat+beat/2,0.75)
        add(hat(),t+q*beat+beat/4,0.4); add(hat(),t+q*beat+3*beat/4,0.4)
    add(clap(),t+beat,0.7); add(clap(),t+3*beat,0.7)
    for off,f in ((0.75,240),(1.25,180),(2.25,240),(2.75,300),(3.75,180)): add(conga(f),t+off*beat,0.6)
    t+=bar
out/=np.max(np.abs(out))+1e-9; out*=0.89
pcm=(out*32767).astype(np.int16); st=np.stack([pcm,pcm],1)
w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
