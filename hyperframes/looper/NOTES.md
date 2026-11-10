# Looper / Build-Up — notas de produção

## Material (2026-11-10)
- `assets/raw/c-studio.mp4` (5,08 s, 24 fps) = **Take 1**: "Viu a cara dele ficando louca? É o teu build-up subindo junto." (fala 0,36–4,95)
- `assets/raw/b-studio.mp4` (7,93 s) = **Take 2**: "É o Looper Build-Up da Kalox. Clica em Capture, gira o Intensity e as
  repetições aceleram." (fala 0,2–7,72)
- `assets/raw/a-selfie.mp4` (7,93 s) = **Take 3**: "No drop, um clique e volta ao normal. Comenta drop, que eu te…" — o Veo
  cortou o "mando" (boca fecha em 6,2 s). Uso só até "Comenta drop." (corte em 5,45 s, antes do "que" em 5,55 s).
- Os três: moletom preto de gola redonda, LED branco-gelo, ring light, mãos vazias, mesmo rosto.
- `assets/audio/vst-build.mp3` (31 s): som real do plugin. Faixa com o Looper ligado; 17,3–19,28 s o build final
  (agudos cortados, repetições acelerando); **drop em ~19,28 s** (kick a 128 BPM, 0,469 s).

## Fala para o Voice Changer
`assets/voice/looper-fala-para-voice-changer.wav` (17,4 s) = c[0–4,95] + b[0–7,85] + a[0,85–5,45], tempo final da edição.

## Edição v1 (HyperFrames, `film/`)
- Voz: `looper-voz-voicechanger-v2.wav` (2ª versão do usuário, "mais certa"); atraso constante de 30 ms → media-start 0,03.
- Abertura (0–2,8 s): as 3 telas reais (0% READY → 50% BUILD 1/16 em 0,72 s → 100% FULL ROLL 1/64 em 1,95 s) sobre o
  som real do plugin (`vst-build.mp3` a partir de 16,58 s); o drop (~19,38 s do áudio) cai no corte para o Take 1.
- Take 2: o plugin inteiro a 82% abaixo do rosto (10,15–15,5 s): destaque no CAPTURE ("clica em Capture"), no botão
  ("gira o Intensity"), muda para 100% em "aceleram". Sem legenda nesse trecho (a interface mostra as palavras).
- Take 3 cortado em "Comenta drop." (o Veo cortou o "que eu te mando"). Cartela: interface em 100% + título + COMENTA DROP,
  com o drop do plugin por baixo.
- Entrega em 1,1× (master `--fps 300/11`): `out/looper-v1-1.1x.mp4` (20,6 s, -15,5 LUFS, pico -1,3 dB). Mapeamento
  1 quadro do master por quadro de saída. Sincronia medida no master com janelas alinhadas ao início da fala:
  0 ms, 26/26 janelas em ±40 ms. (Janelas desalinhadas, começando no 0 do filme, caem em pausas e dão desvios falsos.)

## Edição v2 — plugin animado de verdade
- O usuário achou a troca entre as 3 telas paradas "bugada" e mandou o tutorial do macOS (`assets/rec/plugin-tela.mov`).
- Uso só a janela do plugin (recorte 1080×760 a partir de y=560, sem os textos do tutorial):
  - abertura: 16,2–20,4 s do tutorial ajustado a 2,8 s (carinha → olhos em X junto com o build);
  - Take 2: 13,7–15,93 + 16,18–20,4 s ajustados a 5,35 s (clique no CAPTURE em ~10,8 s, botão girando em ~12,0 s,
    olhos em X em ~14,3 s do filme). Pula os efeitos de transição do tutorial (faixa roxa em ~16,0 e ~20,5 s).
- Sincronia no master: 0 ms (26/26 janelas). Mapeamento 1,1×: 468/470 quadros diretos. Saídas:
  `out/looper-v2-master.mp4` e `out/looper-v2-1.1x.mp4` (20,6 s, -15,5 LUFS, pico -1,3 dB).

## Edição v3 — só a fala acelera
- O usuário: "não acelera a música e nem o plugin, acelera só o vídeo meu falando". Agora abertura (0–2,8 s: plugin +
  build/drop) e cartela (drop) ficam em 1×; só os takes (2,8–20,2 s do filme) saem em 1,1×.
- `film/assemble.py SPEED master30 masterFast out`: imagem da abertura/cartela do master de 30 fps e da fala do master a
  `--fps 300/11`; áudio refeito (voz com atempo 1,1, efeitos nos tempos novos, som do plugin em 1×).
- Cauda do drop encurtada (some em 0,35 s depois do corte) para não cobrir o "Viu".
- Conferido: 629/629 quadros no lugar certo; voz × fala original 0 ms (25/26, a de fora cai no "ding"); transcrição ok;
  -15,9 LUFS, pico -1,6 dB. Saída: `film/out/looper-v3-1.1x.mp4` (21,0 s).

## Edição v4 (pedido: música de fundo, legenda em tudo, início sincronizado com a música, animações)
- Drop real do áudio: kick em 19,415 s (não 19,38). Abertura (2,8 s) = áudio 16,615→19,415; a gravação foi montada
  nas batidas do build: mouse → clique no CAPTURE na 1ª batida (0,99 s), botão girando/sorriso, olhos em X completos
  ~2,7 s, corte no drop. O plugin dá um pulinho em cada batida (0,99/1,10/1,22/1,35/1,59/1,83/2,08/2,20/2,43/2,63).
- Música de fundo = a própria faixa do plugin em 1× do começo ao fim: 0,8 até o drop, abaixa para 0,1 sob a voz,
  sobe para 0,5 na cartela (loop de 6 compassos pós-drop). Renderizada à parte (no grafo grande o loop sumia).
- Áudio: amix com a música como 1ª entrada (`duration=first`) — antes o áudio começava em 2,757 s. Ganho fixo para
  -15 LUFS + limiter (o loudnorm dinâmico achatava o drop).
- Legendas também no trecho do plugin (entre o queixo e o plugin); entradas/saídas animadas em legendas, nome, plugin
  e cartela. Saída: `film/out/looper-v4-1.1x.mp4` (20,97 s, -15,3 LUFS, pico -1,3 dB); voz 0 ms (25/26).
