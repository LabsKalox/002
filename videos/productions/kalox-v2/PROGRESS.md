# Progresso — KaloxSooth v2

## Entregue
- `out/kalox-v2-r2.mp4`: 26,9 s, 1080×1920, 30 fps, -16,9 LUFS (pico -0,4 dBFS).
  Build `bld_20261027T024756082Z_A13C5DF3C0`. Sem custo: tudo renderizado localmente.

## Como está montado
- Fonte: `authors/main.svml`; cores e tamanhos: `recipes/look.svs`; render: `runs/final.svrun`.
- A-roll: `assets/raw/aroll-preto-B.mp4` (Veo 3, estúdio preto), 0–222f, com zoom na frase "nessa mix ardida" (107–154f).
- Tela: IMG_1740 (src 59f) → IMG_1739 (src 61f) → IMG_1741 (src 115f), offsets medidos por
  correlação de áudio com o original; zoom na entrada de cada plano e no "NADA." (590–608f).
- Headline fixa com "DE GRAÇA" em azul-gelo (#A6ECFF, combina com o LED e com a interface do plugin).
- Legendas em pop, palavras-chave em azul-gelo; etiquetas "LIGA O SOM E ESCUTA" e
  "OLHA O CORTE NOS PICOS" nas pausas de prova; pílula "BAIXA GRÁTIS · LINK NA BIO".
- Som: vozes com ganho por loudness medido; whoosh sintetizado nos cortes; impacto no "NADA.".
- Vinheta e flash branco na troca para a tela.

## Notas técnicas
- Transcrição: Whisper small via sherpa-onnx (modelo das releases do GitHub; o huggingface.co é
  bloqueado). Tempos das legendas em frames, escritos à mão no Timeline.
- Text-fine: o Stroke precisa vir antes do Fill (senão cobre a cor); quebras manuais com
  `<typo:Break/>` nas legendas longas (a quebra automática partiu palavra junto de um Span).
- Montserrat via `@fontsource-variable/montserrat`.

## Próximo
- Feedback do usuário sobre ritmo, cores e textos das etiquetas.
- Para virar template: trocar os clipes e o bloco de Timeline/legendas a cada novo vídeo.
