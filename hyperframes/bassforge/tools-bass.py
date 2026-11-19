"""Toca as notas REAIS do print do BassForge ("Obsidian Wave", Cm, 2 compassos, 120 bpm) num baixo de house sintetizado.
Notas lidas do piano roll (assets/ui/plugin-daw.png): compasso 1 começa em x=80, compasso 2 em x=1033 (953 px = 16 semicolcheias);
linha do C1 em y≈631, 33,5 px por semitom. Altura: C1 = MIDI 36 (65,4 Hz, convenção do Ableton)."""
import json, wave, sys, numpy as np
SR = 48000; BPM = 120; STEP = 60 / BPM / 4            # semicolcheia = 0,125 s
X0, BARPX, C1Y, SEMI = 80, 953, 631, 33.5
ui = json.load(open("film/assets/ui/stage.json"))
notes = []
for n in ui["notes"]:                                  # caixas com 10 px de margem em volta da pílula
    x0, x1 = n["x"] + 10, n["x"] + n["w"] - 10; yc = n["y"] + n["h"] / 2
    st = round((x0 - X0) / (BARPX / 16))
    ln = max(0.45, (x1 - x0) / (BARPX / 16) + 0.15)
    midi = 36 + round((C1Y - yc) / SEMI)
    notes.append((st, ln, midi))
notes.sort()
print("notas (semicolcheia, duração, MIDI):", notes)
dur = 32 * STEP; N = int(SR * dur); out = np.zeros(N)
for st, ln, m in notes:
    f = 440 * 2 ** ((m - 69) / 12); L = ln * STEP; n = int(SR * (L + 0.06)); t = np.arange(n) / SR
    fc = 260 + 1300 * np.exp(-t / 0.09)               # filtro abre no ataque e fecha (pluck de house)
    s = np.zeros(n)
    for k in range(1, 40):
        if k * f > 6000: break
        s += (1 / k) * np.sin(2 * np.pi * k * f * t) / (1 + (k * f / fc) ** 4)
    s += 0.55 * np.sin(2 * np.pi * f * t)              # corpo/sub
    env = np.minimum(1, t / 0.004) * np.where(t < L, 1.0, np.exp(-(t - L) / 0.02))
    s = np.tanh(1.6 * s * env)
    i = int(round(st * STEP * SR)); j = min(N, i + n); out[i:j] += s[: j - i]
out /= np.max(np.abs(out)) + 1e-9; out *= 0.9
pcm = (out * 32767).astype(np.int16); st2 = np.stack([pcm, pcm], 1)
w = wave.open(sys.argv[1], "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st2.tobytes()); w.close()
