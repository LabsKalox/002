"""Anúncio 3 — monta as peças a partir dos takes do Veo.

Cada trecho de fala é cortado (imagem e áudio juntos, no mesmo ponto), alinhado aos quadros de 24 fps da fonte.
A 1,25× os 24 fps da fonte viram exatamente 30 fps (1 quadro de saída por quadro de entrada: nada repete, nada pula).

Saídas (em assets/):
  voice/anuncio3-fala-para-voice-changer.wav   fala a 1x, trechos em sequência, no tempo da edição (vai ao ElevenLabs)
  voice/voz-temp-veo-1.25x.wav                  mesma fala, acelerada 1,25x (voz provisória do Veo, só p/ conferir)
  raw/face-1.25x.mp4                            imagem dos trechos com rosto (A, B, C) acelerada, 30 fps constante
  timeline.json                                 início/fim (s) de cada trecho já no tempo final
"""
import json, subprocess

SPEED = 1.25
SRC_FPS = 24
PAD_B, PAD_A = 0.07, 0.10
HOLD_END = 0.5
LEAD_FRAMES = 9  # preparação de imagem antes da 1ª palavra (boca fechada -> abrindo); só vídeo, o áudio não muda
LEAD_RANGE = (16, 25)  # t1b: quadros 16-24 (boca fechada, abre no 21-22); o quadro 25-30 é a boca aberta parada, pulado (invisível)

# (id, take, início da fala, fim da fala, texto, tem rosto na tela)
SEGS = [
    ("A1", "t1b", 1.36, 3.28, "Esse plugin cria um riser", True),
    ("A2", "t1b", 3.78, 4.42, "de vocal", True),
    ("A3", "t1b", 5.10, 5.78, "com um clique.", True),
    ("B1", "t2", 1.01, 4.07, "Ele faz o reverse de um a quatro compassos,", True),
    ("B2", "t2", 4.47, 6.66, "com chorus, tremolo e phone.", True),
    ("C2", "t3", 2.12, 4.25, "Sem desenhar automação nenhuma.", True),
    ("D1", "t4", 1.05, 3.87, "Nove e noventa e nove, pagamento único.", False),
    ("D2", "t4", 4.56, 6.06, "Mac e Windows.", False),
    ("E1", "t5", 0.19, 1.14, "Compra pelo celular,", False),
    ("E2", "t5", 1.76, 3.08, "o link vai pro seu e-mail,", False),
    ("E3", "t5", 3.89, 4.95, "e você baixa no PC.", False),
    ("E4", "t5", 5.44, 6.86, "Toca em Saiba mais.", False),
]

def run(cmd):
    subprocess.run(cmd, check=True)

frames = []  # (id, take, start_frame, n_frames, text, face)
for sid, take, a, b, text, face in SEGS:
    f0 = round((a - PAD_B) * SRC_FPS)
    f1 = round((b + PAD_A) * SRC_FPS)
    frames.append((sid, take, f0, f1 - f0, text, face))

# ---- áudio: guia a 1x e voz provisória a 1,25x
inputs, parts, labels = [], [], []
takes = sorted({f[1] for f in frames})
idx = {t: i for i, t in enumerate(takes)}
for t in takes:
    inputs += ["-i", f"assets/raw/{t}.mp4"]
for n, (sid, take, f0, k, text, face) in enumerate(frames):
    s, d = f0 / SRC_FPS, k / SRC_FPS
    parts.append(f"[{idx[take]}:a]atrim=start={s:.6f}:duration={d:.6f},asetpts=PTS-STARTPTS,aresample=48000,"
                 f"afade=t=in:d=0.012,afade=t=out:st={d-0.02:.6f}:d=0.02[a{n}]")
    labels.append(f"[a{n}]")
fc = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(labels)}:v=0:a=1[g]"
run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[g]", "-ac", "1", "-c:a", "pcm_s16le",
     "assets/voice/anuncio3b-fala-para-voice-changer.wav"])
run(["ffmpeg", "-v", "error", "-y", "-i", "assets/voice/anuncio3b-fala-para-voice-changer.wav", "-af", f"atempo={SPEED}",
     "assets/voice/voz-temp-veo-b-1.25x.wav"])

# ---- imagem dos trechos com rosto (um quadro de saída por quadro da fonte)
vin, vparts, vlab = [], [], []
face_frames = [f for f in frames if f[5]]
for n, (sid, take, f0, k, text, face) in enumerate(face_frames):
    vin += ["-i", f"assets/raw/{take}.mp4"]
    if n == 0:  # preparação (quadros LEAD_RANGE) + fala; a boca aberta parada entre os dois é pulada
        a, b = LEAD_RANGE
        assert b - a == LEAD_FRAMES
        vparts.append(f"[{n}:v]split=2[s{n}a][s{n}b]")
        vparts.append(f"[s{n}a]trim=start_frame={a}:end_frame={b},setpts=(PTS-STARTPTS)*{SRC_FPS}/30,fps=30,format=yuv420p[l{n}]")
        vparts.append(f"[s{n}b]trim=start_frame={f0}:end_frame={f0+k},setpts=(PTS-STARTPTS)*{SRC_FPS}/30,fps=30,format=yuv420p[m{n}]")
        vparts.append(f"[l{n}][m{n}]concat=n=2:v=1:a=0[v{n}]")
    else:
        vparts.append(f"[{n}:v]trim=start_frame={f0}:end_frame={f0+k},setpts=(PTS-STARTPTS)*{SRC_FPS}/30,fps=30,format=yuv420p[v{n}]")
    vlab.append(f"[v{n}]")
vfc = ";".join(vparts) + ";" + "".join(vlab) + f"concat=n={len(vlab)}:v=1:a=0[v]"
run(["ffmpeg", "-v", "error", "-y", *vin, "-filter_complex", vfc, "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "14",
     "-r", "30", "assets/raw/face-1.25x.mp4"])

# ---- linha do tempo final (segundos)
t = 0.0
tl = []
for sid, take, f0, k, text, face in frames:
    dur = k / 30.0
    tl.append({"id": sid, "take": take, "start": round(t, 4), "end": round(t + dur, 4), "text": text, "face": face,
               "src_start": f0 / SRC_FPS})
    t += dur
total = t + HOLD_END
json.dump({"speed": SPEED, "speech_end": round(t, 4), "total": round(total, 4), "segs": tl},
          open("assets/timeline.json", "w"), ensure_ascii=False, indent=1)
print(f"fala acelerada: {t:.2f} s | total com {HOLD_END}s de respiro final: {total:.2f} s")
for s in tl:
    print("%s %5.2f–%5.2f  %s %s" % (s["id"], s["start"], s["end"], "[rosto]" if s["face"] else "[arte] ", s["text"]))
