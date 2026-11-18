# Vocal Riser — anúncio 3 "Escuta esse riser de vocal" (≤ 18 s)

## Takes (18/11): t1…t5 (Veo), blusa preta manga longa, estúdio escuro sem LED, mãos livres
- t1 "Escuta esse riser de vocal. [pausa 2 s] Isso aqui foi um clique." / t2 "Ele faz o reverse de um a quatro compassos,
  com chorus, tremolo e phone." / t3 "E dá pra ajustar depois. Sem desenhar automação nenhuma. [+ frase extra descartada
  'Isso aqui foi um clique']" / t4 "Nove e noventa e nove, pagamento único. Mac e Windows." / t5 "Compra pelo celular, o
  link vai pro seu e-mail, e você baixa no PC. Toca em Saiba mais."

## Como coube em 18 s (fala 16,7 s + 0,5 s de respiro = 17,2 s)
- `build_assets.py` corta cada frase (imagem e áudio no mesmo ponto, alinhado aos 24 fps da fonte), tira as pausas e
  acelera **1,25×**: 24 fps × 1,25 = 30 fps → 1 quadro de saída por quadro da fonte (nada repete, nada pula).
- "E dá pra ajustar depois" saiu da fala (ficou como texto AJUSTA TUDO DEPOIS 🎛️): era o corte previsto no roteiro.
- Voz: `assets/voice/anuncio3-voz-voicechanger.wav` (Voice Changer), atraso 20 ms cortado, `atempo 1.25`.

## Conferido no arquivo final (`film/out/vocalriser-anuncio3-v1.mp4`)
- voz × fala original: 27/27 janelas em ±40 ms; imagem 100% dos quadros no lugar (A1, A2, B1, B2, C2); transcrição completa;
  -15,3 LUFS, pico -1,7 dB; 17,2 s, 1080×1920, 30 fps.
- A fonte NotoColorEmoji.ttf (10 MB) não está no git (copiar de /usr/share/fonts/truetype/noto/ antes de renderizar).
