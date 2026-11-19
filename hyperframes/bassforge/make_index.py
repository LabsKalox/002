"""Gera film/index.html a partir de assets/timeline.json (tempos da fala) e film/assets/ui/stage.json (notas/clip)."""
import json
TL = json.load(open("assets/timeline.json")); UI = json.load(open("film/assets/ui/stage.json"))
LEAD = TL["lead"]; S = {s["id"]: {k: (v + LEAD if isinstance(v, float) else v) for k, v in s.items()} for s in TL["segs"]}
TOTAL = round(TL["total"] + LEAD, 3); FACE_END = round(TL["end"] + LEAD, 3)
VOICE_START = round(LEAD - 0.04, 3)          # voz 40 ms adiantada (o áudio do Veo sai atrás da boca)
DY = -340                                    # rosto sobe: olhos ~y390, queixo <= ~776; legenda 795; plugin 865–1250
CARD = dict(x=65, y=865, w=950, h=385)
BPM_BAR = 2.0                                # 120 bpm: 1 compasso = 2 s; piano roll = 2 compassos
ROLL_X0, ROLL_X1 = 80, 1990
f = lambda x: f"{x:.3f}"

A1, A2, A3 = S["A1"], S["A2"], S["A3"]; B1, B2, B3 = S["B1"], S["B2"], S["B3"]; C1 = S["C1"]
D1, D2, D3, D4 = S["D1"], S["D2"], S["D3"], S["D4"]
t_click = A3["speech_end"] - 0.25            # "cli-que"
t_back = t_click + 0.18
t_notes = t_back + 0.35
t_sweep2 = t_notes + 0.1
t_drag = C1["start"] + 0.45                  # "Arrasta"
t_land = C1["speech_end"] - 0.05
BAR = lambda k: LEAD + 2.0 * k            # início do compasso k (0 = primeiro), 120 bpm
T_DROP = None                              # definido abaixo: a bateria entra logo que o trecho de baixo da abertura sai
import os
BASS = {"afro": "assets/audio/bass-afro.wav"}
HAS_BASS = all(os.path.exists("film/" + v) for v in BASS.values())
BASS_END = A1["speech_end"] + 0.02            # fim de "baixo"
T_DROP = BASS_END                          # depois disso volta o áudio normal (bateria + efeitos), sem baixo

notes_html = "\n".join(f'          <img class="note" id="n{n["i"]}" src="assets/ui/note{n["i"]}.png" alt="" style="left:{n["x"]}px;top:{n["y"]}px;width:{n["w"]}px;height:{n["h"]}px" />' for n in UI["notes"])
c = UI["clip"]

def sweep(t0, t1):
    """playhead de t0 a t1 (s), começando no compasso 1; brilho em cada nota quando o playhead passa"""
    span = (t1 - t0); x1 = ROLL_X0 + (ROLL_X1 - ROLL_X0) * span / (2 * BPM_BAR)
    js = [f'tl.set("#playhead", {{ x: 0, opacity: 1 }}, {f(t0)}).to("#playhead", {{ x: {x1 - ROLL_X0:.1f}, duration: {f(span)}, ease: "none" }}, {f(t0)}).set("#playhead", {{ opacity: 0 }}, {f(t1)});']
    for n in UI["notes"]:
        tn = t0 + (n["x"] + 10 - ROLL_X0) / (ROLL_X1 - ROLL_X0) * 2 * BPM_BAR
        if tn < t1 - 0.05:
            js.append(f'tl.fromTo("#n{n["i"]}", {{ filter: "brightness(1.9) saturate(1.3)" }}, {{ filter: "brightness(1) saturate(1)", duration: 0.35, ease: "power2.out", immediateRender: false }}, {f(tn)});')
    return "\n      ".join(js)

def cam(t, cx, cy, s, dur=0.5, ease="power2.inOut"):
    return f'tl.to("#stage", {{ x: {CARD["w"]/2 - cx*s:.1f}, y: {CARD["h"]/2 - cy*s:.1f}, scale: {s}, duration: {dur}, ease: "{ease}" }}, {f(t)});'
def camset(t, cx, cy, s):
    return f'tl.set("#stage", {{ x: {CARD["w"]/2 - cx*s:.1f}, y: {CARD["h"]/2 - cy*s:.1f}, scale: {s} }}, {f(t)});'

face_js = []
zooms = {"A1": (1.0, 1.03), "A2": (1.07, 1.09), "A3": (1.0, 1.04), "B1": (1.06, 1.08), "B2": (1.0, 1.02), "B3": (1.06, 1.08),
         "C1": (1.0, 1.04), "D1": (1.07, 1.09), "D2": (1.0, 1.03), "D3": (1.06, 1.08), "D4": (1.0, 1.04)}
for sid, (z0, z1) in zooms.items():
    s = S[sid]; t0 = 0.0 if sid == "A1" else s["start"]; d = s["end"] - t0 - 0.01
    face_js.append(f'tl.set("#face", {{ scale: {z0} }}, {f(t0)}).to("#face", {{ scale: {z1}, duration: {f(d)}, ease: "none" }}, {f(t0)});  // {sid} {s["text"]}')

MENU_ROWS = {"AFRO HOUSE": 196, "DEEP HOUSE": 284, "TECH HOUSE": 328}
menu_js = []
for (name, y), seg in zip(MENU_ROWS.items(), (B1, B2, B3)):
    t = seg["start"] + 0.06
    menu_js.append(f'tl.to("#menu .hl", {{ y: {y - 196}, duration: 0.16, ease: "power2.out" }}, {f(t)}).to("#menu .check", {{ y: {y - 196}, duration: 0.16, ease: "power2.out" }}, {f(t)});')
    menu_js.append(f'tl.fromTo("#menu .hl", {{ opacity: 1 }}, {{ opacity: 0.55, duration: 0.5, ease: "power1.out", immediateRender: false }}, {f(t + 0.16)});')

GHOST_FROM = (1205 - c["w"] / 2 - c["x"], 1460 - c["h"] / 2 - c["y"])

sfx = [("s-pop1", "pop", A2["start"], 0.14), ("s-click", "click", t_click, 0.32), ("s-tick-notes", "tick", t_notes, 0.16),
       ("s-t1", "tick", B1["start"] + 0.06, 0.2), ("s-t2", "tick", B2["start"] + 0.06, 0.2),
       ("s-t3", "tick", B3["start"] + 0.06, 0.2), ("s-whoosh2", "whoosh", t_drag + 0.15, 0.18), ("s-pop2", "pop", t_land, 0.2),
       ("s-whoosh3", "whoosh", D1["start"] - 0.08, 0.18), ("s-pop3", "pop", D2["start"] + 0.05, 0.16), ("s-pop4", "pop", D3["start"] + 0.05, 0.16),
       ("s-pop5", "pop", D4["start"] + 0.05, 0.18), ("s-ding", "ding", D4["speech_end"] + 0.05, 0.18)]
sfx_html = "\n".join(f'      <audio id="{i}" class="clip" src="assets/sfx/{n}.wav" data-start="{f(t)}" data-duration="{f(min(0.6, TOTAL - t))}" data-track-index="{5 + k % 2}" data-volume="{v}"></audio>' for k, (i, n, t, v) in enumerate(sfx))

def bass_clips():
    if not HAS_BASS:
        return "      <!-- BAIXO DO BASSFORGE: entra quando existirem film/assets/audio/bass-afro|deep|tech.wav (2 compassos, 120 bpm, do tempo 1) -->"
    beat = 0.5
    nb = lambda t: LEAD + beat * round((t - LEAD) / beat)       # tempo mais próximo
    plan = [("afro", LEAD, BASS_END, 0.0, 0.32)]           # só na abertura: "Escuta essa linha de baixo" (entra e sai)
    out, n = [], 0
    for k, a, b, ms, v in plan:
        if ms is None: ms = ((a - LEAD) % 4.0)                   # mantém a fase do compasso
        while b - a > 0.02:                                      # o arquivo tem 4 s: repete em loop no fim dele
            d = min(b - a, 4.0 - ms)
            out.append(f'      <audio id="bass{n}" class="clip" src="{BASS[k]}" data-start="{f(a)}" data-duration="{f(d)}" data-media-start="{f(ms)}" data-track-index="{3 + n % 2}" data-volume="{v}"></audio>')
            a, ms, n = a + d, 0.0, n + 1
    return "\n".join(out)
bass_html = bass_clips()

html = f'''<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Mont"; src: url("assets/fonts/montserrat-latin-wght-normal.woff2") format("woff2"); font-weight: 100 900; font-style: normal; }}
      :root {{ --brand: #8b5cf6; --brand2: #c4b5fd; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #000; }}
      #root {{ position: relative; width: 100%; height: 100%; font-family: "Mont", sans-serif; overflow: hidden; background: #000; }}
      .shot {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; transform-origin: 50% 38%; }}
      #fadebot {{ position: absolute; left: 0; top: 1380px; width: 1080px; height: 540px; background: linear-gradient(180deg, rgba(0,0,0,0) 0, #000 200px, #000 100%); z-index: 2; }}
      .cap {{ position: absolute; left: 65px; right: 65px; top: 795px; text-align: center; z-index: 30; }}
      .cap .in {{ display: inline-block; color: #fff; font-weight: 900; line-height: 1.1; white-space: nowrap; paint-order: stroke fill; -webkit-text-stroke: 14px #000; text-shadow: 0 8px 18px rgba(0,0,0,.7); }}
      #card {{ position: absolute; left: {CARD["x"]}px; top: {CARD["y"]}px; width: {CARD["w"]}px; height: {CARD["h"]}px; border-radius: 24px; overflow: hidden; z-index: 20;
              background: #14121c; box-shadow: 0 0 0 3px rgba(139,92,246,.75), 0 0 44px rgba(139,92,246,.45), 0 24px 70px rgba(0,0,0,.8); }}
      #stage {{ position: absolute; left: 0; top: 0; width: 2000px; height: 1591px; transform-origin: 0 0; }}
      #stage > img.base {{ position: absolute; left: 0; top: 0; width: 2000px; height: 1591px; display: block; }}
      .note {{ position: absolute; display: block; transform-origin: 50% 50%; }}
      #playhead {{ position: absolute; left: {ROLL_X0}px; top: 345px; width: 4px; height: 405px; background: #e9e2ff; box-shadow: 0 0 14px #a78bfa, 0 0 30px rgba(139,92,246,.8); opacity: 0; }}
      #gen {{ position: absolute; left: 905px; top: 1020px; width: 325px; height: 325px; transform-origin: 50% 50%; }}
      #genring {{ position: absolute; left: 918px; top: 1032px; width: 300px; height: 300px; border-radius: 50%; border: 6px solid var(--brand2); box-shadow: 0 0 40px var(--brand), inset 0 0 30px rgba(139,92,246,.6); opacity: 0; transform-origin: 50% 50%; }}
      #drag {{ position: absolute; left: 1100px; top: 1355px; width: 210px; height: 210px; transform-origin: 50% 50%; }}
      #clipReal, #ghost {{ position: absolute; left: {c["x"]}px; top: {c["y"]}px; width: {c["w"]}px; height: {c["h"]}px; }}
      #clipReal {{ opacity: 0; }}
      #ghost {{ opacity: 0; transform-origin: 50% 50%; }}
      #ghost img {{ width: 100%; height: 100%; display: block; border-radius: 6px; box-shadow: 0 0 30px rgba(139,92,246,.9); opacity: .92; }}
      #ghost svg {{ position: absolute; left: 55%; top: 55%; width: 70px; height: 70px; filter: drop-shadow(0 3px 6px rgba(0,0,0,.7)); }}
      #menu {{ position: absolute; left: {(CARD["w"] - 802*0.85)/2:.0f}px; top: 0; width: 802px; height: 680px; transform-origin: 0 0; opacity: 0; }}
      #menu img {{ position: absolute; left: 0; top: 0; width: 802px; height: 680px; display: block; }}
      #menu .hl {{ position: absolute; left: 50px; top: 175px; width: 545px; height: 42px; border-radius: 8px; background: rgba(139,92,246,.35); box-shadow: 0 0 22px rgba(139,92,246,.55); }}
      #menu .check {{ position: absolute; left: 62px; top: 176px; color: #fff; font: 700 30px/40px "Mont", sans-serif; }}
      #menu .lblbg {{ position: absolute; left: 178px; top: 53px; width: 168px; height: 28px; background: rgb(53,51,72); }}
      #menu .lbl {{ position: absolute; left: 61px; top: 50px; width: 400px; text-align: center; color: #fff; font: 700 17px/34px "Mont", sans-serif; letter-spacing: 1.5px; transform-origin: 50% 50%; }}
      #panel {{ position: absolute; left: 0; top: 0; width: {CARD["w"]}px; height: {CARD["h"]}px; opacity: 0; background: radial-gradient(ellipse at 50% 40%, #2a2140, #14121c 75%); }}
      #panel .wm {{ position: absolute; left: {(CARD["w"]-490)/2:.0f}px; top: {(CARD["h"]-120)/2:.0f}px; width: 490px; height: 120px; transform-origin: 50% 50%; }}
      #panel .row {{ position: absolute; left: 0; right: 0; text-align: center; color: #fff; font-weight: 900; white-space: nowrap; opacity: 0; }}
      #panel .price {{ top: 108px; font-size: 128px; line-height: 1; letter-spacing: -3px; text-shadow: 0 0 40px rgba(139,92,246,.7); }}
      #panel .once {{ top: 262px; }}
      #panel .once span, #panel .cta span {{ display: inline-block; padding: 14px 40px; border-radius: 60px; background: var(--brand); color: #fff; font-size: 44px; letter-spacing: 2px; box-shadow: 0 0 34px rgba(139,92,246,.6); }}
      #panel .os {{ top: 140px; font-size: 46px; letter-spacing: 1px; }}
      #panel .fmt {{ top: 220px; font-size: 40px; color: var(--brand2); letter-spacing: 3px; }}
      #panel .cta {{ top: 150px; }}
      #panel .cta span {{ font-size: 64px; padding: 22px 64px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <!-- Rosto em tela cheia (sem bordas), subido para a faixa segura. 1,25x: cada quadro de 24 fps = 1 quadro de 30 fps -->
      <video id="face" class="clip shot" src="assets/raw/face-1.25x.mp4" data-start="0" data-duration="{FACE_END}" data-media-start="0" data-track-index="0" muted playsinline style="z-index: 1"></video>
      <div id="fadebot" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="9"></div>

      <!-- Voz do Lucas (Voice Changer do diálogo do Veo), 30 ms do ElevenLabs cortados, acelerada 1,25x, 40 ms adiantada -->
      <audio id="voice" class="clip" src="assets/voice/voz-lucas-1.25x.wav" data-start="{VOICE_START}" data-duration="15.95" data-media-start="0" data-track-index="1" data-volume="1"></audio>
      <!-- Bateria 120 bpm (sintetizada, sem baixo) -->
      <audio id="drums" class="clip" src="assets/audio/drums-120.wav" data-start="{f(T_DROP)}" data-duration="{f(TOTAL - T_DROP)}" data-media-start="{f(T_DROP - LEAD)}" data-track-index="2" data-volume="0.16" data-fade-out="0.6"></audio>
{bass_html}
{sfx_html}

      <!-- Plugin (interface real animada) -->
      <div id="card" class="clip" data-start="0.6" data-duration="{f(TOTAL - 0.6)}" data-track-index="8">
        <div id="stage">
          <img class="base" src="assets/ui/stage-base.png" alt="Interface do BassForge" />
{notes_html}
          <div id="playhead"></div>
          <img id="gen" src="assets/ui/gen-btn.png" alt="" /><div id="genring"></div>
          <img id="drag" src="assets/ui/drag-btn.png" alt="" />
          <img id="clipReal" src="assets/ui/clip.png" alt="" />
          <div id="ghost"><img src="assets/ui/clip.png" alt="" /><svg viewBox="0 0 24 24"><path d="M4 2l15 11-6.5 1 3.6 7.2-2.6 1.3-3.6-7.2L4 20z" fill="#fff" stroke="#000" stroke-width="1.4" stroke-linejoin="round"/></svg></div>
        </div>
        <div id="menu"><img src="assets/ui/menu-base.png" alt="Estilos do BassForge" /><div class="hl"></div><div class="check">✓</div></div>
        <div id="panel">
          <img class="wm" src="assets/ui/wordmark-a.png" alt="BassForge by Kalox" />
          <div class="row price">R$ 18,90</div>
          <div class="row once"><span>PAGAMENTO ÚNICO</span></div>
          <div class="row os">macOS · APPLE SILICON + INTEL</div>
          <div class="row fmt">VST3 · AU</div>
          <div class="row cta"><span>SAIBA MAIS</span></div>
        </div>
      </div>

      <!-- Legendas (brancas, contorno preto), entre o queixo e o plugin -->
      <div id="k1" class="clip cap" data-start="0" data-duration="{f(A3['start'])}" data-track-index="7"><span class="in" style="font-size: 52px; letter-spacing: 1px">PLUGIN MIDI · VST3 · AU</span></div>
      <div id="k2" class="clip cap" data-start="{f(t_click - 0.1)}" data-duration="{f(B1['start'] - t_click + 0.1)}" data-track-index="7"><span class="in" style="font-size: 58px">1 CLIQUE</span></div>
      <div id="k3" class="clip cap" data-start="{f(B1['start'])}" data-duration="{f(C1['start'] - B1['start'])}" data-track-index="7"><span class="in" style="font-size: 56px">8 ESTILOS DE HOUSE</span></div>
      <div id="k4" class="clip cap" data-start="{f(t_drag - 0.1)}" data-duration="{f(D1['start'] - t_drag + 0.1)}" data-track-index="7"><span class="in" style="font-size: 56px">ARRASTA PRA DAW</span></div>
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      const pop = (sel, t) => tl.fromTo(sel, {{ scale: 0.5, opacity: 0, y: 30 }}, {{ scale: 1, opacity: 1, y: 0, duration: 0.22, ease: "back.out(2.2)" }}, t);
      const out = (sel, t) => tl.to(sel, {{ scale: 0.8, opacity: 0, y: -14, duration: 0.1, ease: "power2.in" }}, t - 0.1);

      // ---------- rosto: sobe para a faixa segura + zoom-cut a cada trecho (os cortes ficam nas pausas)
      gsap.set("#face", {{ y: {DY} }});
      gsap.set("#panel .wm", {{ scale: 1.6 }});
      {chr(10).join("      " + l for l in face_js).strip()}

      // ---------- legendas
      pop("#k1 .in", 0.05); out("#k1 .in", {f(A3['start'])});
      pop("#k2 .in", {f(t_click - 0.1)}); out("#k2 .in", {f(B1['start'])});
      pop("#k3 .in", {f(B1['start'])}); out("#k3 .in", {f(C1['start'])});
      pop("#k4 .in", {f(t_drag - 0.1)}); out("#k4 .in", {f(D1['start'])});

      // ---------- plugin: entra cedo e fica; câmera passeia pela interface real
      tl.fromTo("#card", {{ y: 80, opacity: 0, scale: 0.94 }}, {{ y: 0, opacity: 1, scale: 1, duration: 0.4, ease: "power3.out" }}, 0.6);
      {camset(0, 740, 547, 0.72)}
      {sweep(LEAD, A1['speech_end'] + 0.02)}
      // "gerou ela com um clique": vai até o GENERATE e aperta
      {cam(A3['start'], 1066, 1170, 0.62, 0.55)}
      tl.to("#gen", {{ scale: 0.92, duration: 0.08, ease: "power2.in" }}, {f(t_click)}).to("#gen", {{ scale: 1, duration: 0.25, ease: "back.out(3)" }}, {f(t_click + 0.08)});
      tl.fromTo("#genring", {{ opacity: 0, scale: 0.9 }}, {{ opacity: 1, scale: 1.12, duration: 0.25, ease: "power2.out", immediateRender: false }}, {f(t_click)}).to("#genring", {{ opacity: 0, duration: 0.35 }}, {f(t_click + 0.3)});
      tl.to(".note", {{ opacity: 0, scale: 0.6, duration: 0.1 }}, {f(t_click)});
      // volta ao piano roll: as notas nascem uma a uma e tocam
      {cam(t_back, 740, 547, 0.72, 0.45)}
      tl.fromTo(".note", {{ opacity: 0, scale: 0.2 }}, {{ opacity: 1, scale: 1, duration: 0.22, ease: "back.out(2.5)", stagger: 0.04, immediateRender: false }}, {f(t_notes)});

      // ---------- estilos: menu real, a seleção desce Afro → Deep → Tech
      tl.to("#stage", {{ opacity: 0, duration: 0.2 }}, {f(B1['start'] - 0.1)});
      tl.fromTo("#menu", {{ opacity: 0, scale: 0.7, y: -80 }}, {{ opacity: 1, scale: 0.85, y: -100, duration: 0.3, ease: "back.out(1.6)", immediateRender: false }}, {f(B1['start'] - 0.05)});
      {chr(10).join("      " + l for l in menu_js).strip()}

      // ---------- arrasta pra DAW: o clip sai do botão e cai na pista
      tl.to("#menu", {{ opacity: 0, duration: 0.2 }}, {f(C1['start'] - 0.05)});
      {camset(C1['start'] - 0.05, 1205, 1270, 0.6)}
      tl.to("#stage", {{ opacity: 1, duration: 0.2 }}, {f(C1['start'] - 0.05)});
      tl.to("#drag", {{ scale: 0.9, duration: 0.1 }}, {f(t_drag)}).to("#drag", {{ scale: 1, duration: 0.2, ease: "back.out(3)" }}, {f(t_drag + 0.1)});
      tl.fromTo("#ghost", {{ opacity: 0, x: {GHOST_FROM[0]:.0f}, y: {GHOST_FROM[1]:.0f}, scale: 0.5 }}, {{ opacity: 1, scale: 0.8, duration: 0.15, immediateRender: false }}, {f(t_drag)});
      tl.to("#ghost", {{ x: 0, y: 0, scale: 1, duration: {f(t_land - t_drag - 0.2)}, ease: "power2.inOut" }}, {f(t_drag + 0.15)});
      {cam(t_drag + 0.15, 1052, 330, 0.55, t_land - t_drag - 0.15)}
      tl.set("#clipReal", {{ opacity: 1 }}, {f(t_land)}).to("#ghost", {{ opacity: 0, duration: 0.15 }}, {f(t_land)});
      tl.fromTo("#clipReal", {{ scale: 1.15, filter: "brightness(1.6)" }}, {{ scale: 1, filter: "brightness(1)", duration: 0.35, ease: "back.out(2)", immediateRender: false }}, {f(t_land)});

      // ---------- preço / Mac / Saiba mais (logo real)
      tl.to("#stage", {{ opacity: 0, duration: 0.2 }}, {f(D1['start'] - 0.1)});
      tl.fromTo("#panel", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, immediateRender: false }}, {f(D1['start'] - 0.1)});
      tl.fromTo("#panel .wm", {{ scale: 1.1, opacity: 0 }}, {{ scale: 1.6, opacity: 1, duration: 0.35, ease: "back.out(1.8)", immediateRender: false }}, {f(D1['start'] - 0.05)});
      tl.to("#panel .wm", {{ scale: 0.72, y: -118, duration: 0.3, ease: "power2.inOut" }}, {f(D2['start'])});
      tl.fromTo("#panel .price", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)", immediateRender: false }}, {f(D2['start'] + 0.05)});
      tl.fromTo("#panel .once", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "back.out(1.8)", immediateRender: false }}, {f(D2['start'] + 0.9)});
      tl.to("#panel .price, #panel .once", {{ opacity: 0, y: -20, duration: 0.15 }}, {f(D3['start'] - 0.05)});
      tl.fromTo("#panel .os", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "back.out(1.8)", immediateRender: false }}, {f(D3['start'] + 0.02)});
      tl.fromTo("#panel .fmt", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "back.out(1.8)", immediateRender: false }}, {f(D3['start'] + 0.2)});
      tl.to("#panel .os, #panel .fmt", {{ opacity: 0, y: -20, duration: 0.15 }}, {f(D4['start'] - 0.05)});
      tl.fromTo("#panel .cta", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.2)", immediateRender: false }}, {f(D4['start'] + 0.02)});
      tl.to("#panel .cta span", {{ scale: 1.07, duration: 0.3, repeat: 3, yoyo: true, ease: "sine.inOut" }}, {f(D4['start'] + 0.4)});

      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
'''
open("film/index.html", "w", encoding="utf-8").write(html)
print("ok total", TOTAL, "clique", round(t_click, 2), "arrasta", round(t_drag, 2), "pousa", round(t_land, 2))
