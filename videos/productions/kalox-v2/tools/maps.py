import json, numpy as np
pts=json.load(open("/tmp/claude-0/-home-user-002/87f6385b-7dc3-5fa8-9d19-914098da7b2e/scratchpad/dtw_map.json"))
f=np.array([p[0] for p in pts]); v=np.array([p[1] for p in pts])*30   # veo frames
for a,b in zip(f,v):
    if 84<=a<=100: print(a, round(b,1))
v=np.maximum.accumulate(v)
def veo(fr): return float(np.interp(fr,f,v))
step=6
def pieces(a,b,cut_jumps=True):
    out=[]; fr=a
    while fr<b:
        nx=min(fr+step,b); s0,s1=veo(fr),veo(nx)
        out.append((fr,nx,s0,s1)); fr=nx
    return out
print("jump scan:")
for fr in range(84,100): print(fr, round(veo(fr),1), round(veo(fr+1)-veo(fr),2))

def build(a,b,first_src=None,step=8):
    out=[]; fr=a
    while fr<b:
        nx=min(fr+step,b); s0=veo(fr) if not (fr==a and first_src is not None) else first_src; s1=veo(nx)
        if s1-s0<1: s1=s0+1
        out.append((fr-a,nx-a,s0,s1)); fr=nx
    return out
def xml(ps):
    return "\n".join(f'      <visual:Map target-from="{t0}f" target-until="{t1}f" source-from="{s0:.2f}f" source-until="{s1:.2f}f"/>' for t0,t1,s0,s1 in ps)
a1=[(0,6,0.0,veo(6))]+[(t0,t1,s0,s1) for t0,t1,s0,s1 in build(6,91)]
a2=build(91,128,first_src=108.0)
tail_start=veo(180)
a3=build(128,180)+[(52,94,tail_start,239.0)]
for n,p in (("a1",a1),("a2",a2),("a3",a3)):
    rates=[(s1-s0)/(t1-t0) for t0,t1,s0,s1 in p]; print(n,"rates %.2f..%.2f"%(min(rates),max(rates)))
json.dump({"a1":xml(a1),"a2":xml(a2),"a3":xml(a3)},open("/tmp/claude-0/-home-user-002/87f6385b-7dc3-5fa8-9d19-914098da7b2e/scratchpad/maps.json","w"))
print(xml(a2))
