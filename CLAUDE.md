# Padrões de vídeo do Lucas (Kalox Audio)

Regras de entrega definidas pelo usuário. Valem para todo vídeo novo deste repositório.

## Entrega
- **Todo vídeo final sai acelerado em 1,2×** (o Vocal Riser saiu em 1,1× a pedido dele, como teste). Monte e
  revise na velocidade normal; no fim, gere o arquivo entregue com imagem e voz aceleradas juntas, preservando o tom.
- **Sem pular quadros:** nunca acelere um master de 30 fps (o `fps=30` descarta 1 quadro a cada 5 no 1,2× e 1 a cada
  10 no 1,1×; a imagem dá "travadas" e a boca parece atrasada). Renderize o master a **30 ÷ velocidade** fps
  (1,2× → `--fps 25`; 1,1× → `--fps 300/11`) e acelere, que cada quadro do master vira um quadro de 30 fps:
  `ffmpeg -i master25.mp4 -filter_complex "[0:v]setpts=PTS/1.2,fps=30[v];[0:a]atempo=1.2,loudnorm=I=-15:TP=-1.5:LRA=11,aresample=48000[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart final-1.2x.mp4`
  (cortes no início: use `trim=start_frame=N` em número inteiro de quadros do master). Confira o mapeamento
  quadro a quadro (nenhum passo de 2) antes de entregar.
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
- Rosto (o personagem é o próprio usuário): sempre partir de uma **foto real dele de boa qualidade** (de frente,
  luz suave), nunca de um quadro extraído de vídeo já gerado (edição em cima de edição envelhece e cria pintas).
  Nos prompts (Gemini e Veo): "jovem de 27 anos, pele lisa, saudável e uniforme, sem rugas, sem manchas, sem
  verrugas; luz suave e frontal tipo ring light, sem sombras duras; nítido, alta qualidade". Veo no modo Quality.
- Voz do usuário: fala original do Veo (já no tempo final do vídeo) → Voice Changer do ElevenLabs com o clone
  dele → volta sem edição. Cortar só o silêncio inicial que o ElevenLabs adiciona. Isso mantém a boca sincronizada
  sem cortar nem acelerar a imagem.
- Não emendar trechos de outra voz/versão no áudio que o usuário mandar.
- Medir a sincronia no arquivo final (não só no plano) antes de dizer que está sincronizado.

## Projetos
- KaloxSooth: `videos/` (Hypit). BankMaster 2.0: `hyperframes/bankmaster/film/` (HyperFrames; notas em `NOTES.md`).
