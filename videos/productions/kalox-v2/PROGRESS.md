# Progresso — KaloxSooth v2

## Entregue
- `out/kalox-v2-r5.mp4`: 26,9 s, legendas brancas, voz do usuário no A-roll, 1080×1920, 30 fps, -16,9 LUFS (pico -0,4 dBFS).
  Build `bld_20261027T031908886Z_8E9150BEB3`. Sem custo: tudo renderizado localmente.

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

## Rodada 4 (pedido do usuário)
- Voz do personagem trocada pela voz do usuário (`references/kalox/source.mp4`, a partir de 0,68 s). O áudio do Veo foi desligado.
- Imagem do Veo reajustada por frase para seguir a voz: F1 9–84f ← Veo 9–99f; F2 86–128f ← 108–144f;
  F3 136–176f ← 155–196f; giro final 176–222f ← 196–239f.
- A mix (IMG_1740) entra em 184f, por baixo do giro para a mesa.
- Headline toda branca com contorno preto grosso (9 e 11 px).
- Pílula de CTA removida (duplicava a legenda); legenda "Link na bio," → "o bagulho é louco.".

## Rodada 5 — lip sync
- O usuário notou a voz atrasada. A causa: na frase 1, a imagem estava até 0,44 s adiantada
  (o encaixe da r4 usava limites de frase medidos por energia).
- Novo encaixe por DTW (MFCC) entre a voz do usuário e a voz original do Veo, que é sincronizada com
  a boca (`tools/dtw.py` gera o mapa; `tools/maps.py` gera os `<visual:Map>` em peças de 8 quadros).
- Corte com zoom no quadro 91, onde o Veo faz uma pausa maior entre "faz" e "nessa".
- `tools/transcribe.py`: Whisper small + VAD via sherpa-onnx (modelos das releases do GitHub).
