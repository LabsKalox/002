# Synthesizes a simple 140 bpm trap loop (kick/808, clap, hats) for the BankMaster teaser bed.
import numpy as np, wave, sys
SR=48000; BPM=140; beat=60/BPM; dur=float(sys.argv[2]) if len(sys.argv)>2 else 24.0
N=int(SR*dur); out=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i<N: out[i:j]+=g*sig[:j-i]
def k808(note_hz=46.25,length=0.9):
    t=np.arange(int(SR*length))/SR
    f=note_hz*(1+2.5*np.exp(-t*40)); ph=2*np.pi*np.cumsum(f)/SR
    return np.tanh(1.8*np.sin(ph))*np.exp(-t*2.6)
def clap():
    t=np.arange(int(SR*0.25))/SR; n=rng.standard_normal(len(t))
    env=np.exp(-t*28)+0.6*np.exp(-np.maximum(t-0.012,0)*40)*(t>0.012)
    # crude bandpass: difference of moving averages
    a=np.convolve(n,np.ones(3)/3,'same')-np.convolve(n,np.ones(24)/24,'same')
    return a*env*0.9
def hat(open_=False):
    t=np.arange(int(SR*(0.18 if open_ else 0.05)))/SR; n=rng.standard_normal(len(t))
    hp=n-np.convolve(n,np.ones(4)/4,'same')
    return hp*np.exp(-t*(18 if open_ else 90))*0.35
bar=4*beat; notes=[46.25,46.25,41.2,51.9]  # F#1 F#1 E1 G#1
t=0.0; b=0
while t<dur:
    n=notes[b%4]
    for off in (0, 1.5*beat, 2.75*beat):
        add(k808(n),t+off,0.9)
    add(clap(),t+beat,0.8); add(clap(),t+3*beat,0.8)
    for s in range(16):
        tt=t+s*beat/4
        if b%2==1 and s in (12,13,14,15):
            for r in range(2): add(hat(),tt+r*beat/8,0.8)
        else: add(hat(open_=(s==14)),tt,0.9 if s%2==0 else 0.6)
    t+=bar; b+=1
out/=np.max(np.abs(out))+1e-9; out*=0.89
pcm=(out*32767).astype(np.int16); st=np.stack([pcm,pcm],1)
w=wave.open(sys.argv[1],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes()); w.close()
