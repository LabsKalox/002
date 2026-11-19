"""BassForge — monta as peças a partir dos 4 takes do Veo (24 fps).

Cada trecho: imagem e áudio cortados no mesmo ponto, alinhados aos quadros de 24 fps. A 1,25x cada quadro da fonte
vira 1 quadro de 30 fps (nada repete, nada pula). Alguns trechos levam uma "cauda" de silêncio (ele calado, sorrindo)
para o baixo do plugin tocar sozinho: a imagem continua e o áudio do guia fica mudo nessa cauda.

Saídas: assets/voice/bassforge-fala-para-voice-changer.wav (1x, vai ao ElevenLabs), assets/voice/voz-temp-veo-1.25x.wav,
assets/raw/face-1.25x.mp4, assets/timeline.json
"""
import json, subprocess

SPEED, SRC_FPS = 1.25, 24
PAD_B, PAD_A = 0.07, 0.10
HOLD_END = 0.5
LEAD_FRAMES = 3  # só imagem: 3 quadros (boca fechada) antes da 1ª palavra, para a voz entrar 40 ms adiantada sem cortar o ataque

# (id, take, início da fala, fim da fala, cauda em segundos NO FILME (já acelerado), texto)
SEGS = [
    ("A1", "take1", 0.42, 1.78, 0.0, "Escuta essa linha de baixo."),
    ("A2", "take1", 3.34, 4.20, 0.0, "Esse plugin"),
    ("A3", "take1", 4.78, 6.54, 1.0, "gerou ela com um clique."),
    ("B1", "take2", 0.46, 1.28, 0.35, "Afro House."),
    ("B2", "take2", 1.70, 2.52, 0.35, "Deep House."),
    ("B3", "take2", 3.32, 4.02, 0.6, "Tech House."),
    ("C1", "take3", 0.10, 1.88, 0.8, "Gostou? Arrasta pra sua DAW."),
    ("D1", "take4", 0.06, 0.88, 0.0, "BassForge."),
    ("D2", "take4", 1.32, 4.26, 0.0, "Dezoito e noventa, pagamento único."),
    ("D3", "take4", 4.58, 5.42, 0.0, "Só pra Mac."),
    ("D4", "take4", 5.82, 7.26, 0.0, "Toca em Saiba mais."),
]

def run(cmd): subprocess.run(cmd, check=True)

frames = []
for sid, take, a, b, tail, text in SEGS:
    f0 = round((a - PAD_B) * SRC_FPS)
    fs = round((b + PAD_A) * SRC_FPS)            # fim da fala (com folga)
    f1 = fs + round(tail * SPEED * SRC_FPS)       # fim da imagem (com a cauda)
    frames.append(dict(id=sid, take=take, f0=f0, fs=fs, f1=f1, text=text))

takes = sorted({f["take"] for f in frames}); idx = {t: i for i, t in enumerate(takes)}
ins = sum((["-i", f"assets/raw/{t}.mp4"] for t in takes), [])

# ---- guia de voz 1x (cauda muda)
parts, labs = [], []
for n, f in enumerate(frames):
    s, d, ds = f["f0"] / SRC_FPS, (f["f1"] - f["f0"]) / SRC_FPS, (f["fs"] - f["f0"]) / SRC_FPS
    chain = (f"[{idx[f['take']]}:a]atrim=start={s:.6f}:duration={d:.6f},asetpts=PTS-STARTPTS,aresample=48000,"
             f"afade=t=in:d=0.012,afade=t=out:st={ds-0.03:.6f}:d=0.03")
    parts.append(chain + f"[a{n}]"); labs.append(f"[a{n}]")
run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(parts) + ";" + "".join(labs) + f"concat=n={len(labs)}:v=0:a=1[g]",
     "-map", "[g]", "-ac", "1", "-c:a", "pcm_s16le", "assets/voice/bassforge-fala-para-voice-changer.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", "assets/voice/bassforge-fala-para-voice-changer.wav", "-af", f"atempo={SPEED}",
     "assets/voice/voz-temp-veo-1.25x.wav"])

# ---- imagem (um quadro de saída por quadro da fonte)
vp, vl = [], []
for n, f in enumerate(frames):
    lead = LEAD_FRAMES if n == 0 else 0
    vp.append(f"[{idx[f['take']]}:v]trim=start_frame={f['f0']-lead}:end_frame={f['f1']},setpts=(PTS-STARTPTS)*{SRC_FPS}/30,fps=30,format=yuv420p[v{n}]")
    vl.append(f"[v{n}]")
run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(vp) + ";" + "".join(vl) + f"concat=n={len(vl)}:v=1:a=0[v]",
     "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "14", "-r", "30", "assets/raw/face-1.25x.mp4"])

# ---- linha do tempo (s, no filme)
t, tl = 0.0, []
for f in frames:
    dur, ds = (f["f1"] - f["f0"]) / 30, (f["fs"] - f["f0"]) / 30
    tl.append({"id": f["id"], "start": round(t, 4), "speech_end": round(t + ds, 4), "end": round(t + dur, 4), "text": f["text"]})
    t += dur
json.dump({"speed": SPEED, "lead": LEAD_FRAMES / 30, "end": round(t, 4), "total": round(t + HOLD_END, 4), "segs": tl}, open("assets/timeline.json", "w"), ensure_ascii=False, indent=1)
for s in tl: print("%s %5.2f–%5.2f (fala até %5.2f)  %s" % (s["id"], s["start"], s["end"], s["speech_end"], s["text"]))
print("fim da imagem %.2f s | total %.2f s" % (t, t + HOLD_END))
