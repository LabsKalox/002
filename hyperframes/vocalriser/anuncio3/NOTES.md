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

## v2 (ajustes pedidos após a v1)
- Selos MAC/WINDOWS: emoji trocado por logos reais em SVG (maçã = simple-icons; Windows = 4 janelas, geometria do logo atual, brancas).
- Sincronia da voz: voz adiantada 40 ms no filme final (`atrim=start=0.07` no 1x antes do `atempo`, com fade-in de 4 ms; antes 0.02).
  Medido: o pipeline (HyperFrames + AAC) não adiciona atraso (+1 ms); `atempo` desloca ~-8 ms. O atraso vinha da fonte:
  Veo (boca × áudio, abertura dos lábios por mediapipe, ~0 a +40 ms tarde) + resíduo do Voice Changer (~+10 ms).
  Final medido: voz -37 ms vs v1; arquivo da voz = final (+1 ms).
- Entrega: -15,3 LUFS, pico -1,6 dBFS, 17,2 s; transcrição completa.
- Se ainda parecer atrasada/adiantada: mudar só o `atrim=start=` de `film/assets/voice/voz-lucas-1.25x.wav` (cada 0,01 = 8 ms no final).

## v3 (início "robótico")
- Causa 1 (imagem): no take o Veo abre a boca no quadro 15 (0,62 s) e a segura aberta, sem som, até a 1ª palavra no quadro 24. O corte da v1/v2
  começava no quadro 23, no fim dessa pose parada: o filme abria com a boca escancarada, sem gesto de abertura.
- Causa 2 (voz): na v2 o adiantamento de 40 ms foi feito cortando 50 ms do começo da voz (`atrim=start=0.07`), comendo o ataque suave do "E".
- Correção: 9 quadros de preparação (quadros 14–22 do T1: boca fechada → abrindo) antes da 1ª palavra (`LEAD_FRAMES` em `build_assets.py`,
  só imagem; guia de voz idêntico, nada a refazer no ElevenLabs). Voz inteira (`atrim=start=0.02`) entrando em 0,26 s no filme
  (= 0,30 s da 1ª palavra −40 ms de adiantamento de sincronia, agora feito pela posição, não por corte). Riser de abertura e "ESCUTA ISSO"
  tocam já em 0 s. Todo o resto desloca +0,3 s (timeline GSAP filha `body` em `LEAD`; `data-start` +0,3).
- Final: 17,5 s, −15,3 LUFS, pico −1,7 dBFS; voz = v2 + 297 ms (sincronia preservada); quadros do rosto sem repetir/pular; transcrição completa.
