# Padrões de vídeo do Lucas (Kalox Audio)

Regras de entrega definidas pelo usuário. Valem para todo vídeo novo deste repositório.

## Entrega
- **Todo vídeo final sai acelerado em 1,2×.** Monte e revise na velocidade normal; no fim, gere o arquivo
  entregue com imagem e voz aceleradas juntas, preservando o tom:
  `ffmpeg -i final.mp4 -filter_complex "[0:v]setpts=PTS/1.2,fps=30[v];[0:a]atempo=1.2[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart final-1.2x.mp4`
- Vertical 1080×1920, 30 fps. Loudness por volta de -15/-16 LUFS, pico abaixo de -1 dB.
- Confira a fala do arquivo acelerado (transcrição) antes de entregar.

## Visual
- Headline fixa no topo e legendas: **brancas com contorno preto** (Montserrat Black). Nada de legenda colorida.
- Sem textos duplicados na tela (ex.: legenda e selo dizendo a mesma coisa ao mesmo tempo).
- Interface e logos do produto sempre reais (nunca inventados); cor de destaque da Kalox/BankMaster: laranja.

## Apresentador (Veo 3) e voz
- Personagem: estúdio todo preto com LED branco-gelo; **moletom todo preto, capuz abaixado, cordões pretos**,
  mãos vazias (sem celular). Prompts em português, fala em português do Brasil (ver
  `hyperframes/bankmaster/VEO-PROMPTS-V2.md`).
- Voz do usuário: fala original do Veo (já no tempo final do vídeo) → Voice Changer do ElevenLabs com o clone
  dele → volta sem edição. Cortar só o silêncio inicial que o ElevenLabs adiciona. Isso mantém a boca sincronizada
  sem cortar nem acelerar a imagem.
- Não emendar trechos de outra voz/versão no áudio que o usuário mandar.
- Medir a sincronia no arquivo final (não só no plano) antes de dizer que está sincronizado.

## Projetos
- KaloxSooth: `videos/` (Hypit). BankMaster 2.0: `hyperframes/bankmaster/film/` (HyperFrames; notas em `NOTES.md`).
