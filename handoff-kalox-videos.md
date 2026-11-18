# 🧠 Contexto Compactado — Vídeos promocionais Kalox Audio (Reels com apresentador Veo + plugin)

**Data da compactação:** 2026-11-18
**Chat original:** ~250 mensagens (sessão longa, várias compactações)
**Repositório:** `LabsKalox/002`, branch `claude/nifty-johnson-j0aj3n` (tudo commitado e enviado)

---

## 1. Objetivo
Produzir Reels verticais (1080×1920) para vender os plugins VST do Lucas (Kalox Audio, produtor de afro/deep/tech house), com um apresentador gerado no Veo 3 (o próprio Lucas), voz dele via ElevenLabs Voice Changer, a interface real do plugin animada e textos grandes queimados. Entregar vídeo final, legenda do post e prompts do Veo.

## 2. Decisões Tomadas
- **Pipeline de voz:** fala original do Veo (no tempo final do vídeo) → Voice Changer do ElevenLabs com o clone dele → volta sem edição; cortar só o atraso inicial (medido com `tools/vrsync.py`). Mantém a boca sincronizada. Nunca emendar outra voz/versão.
- **Rosto:** sempre partir de foto real dele (Gemini/Nano Banana) e travar identidade no prompt; nunca usar quadro de vídeo gerado como base (envelhece, cria pintas).
- **Prompts do Veo:** curtos, fala logo no começo, só português simples, frases de 10–16 palavras. Nomes difíceis (ex.: "Looper Build-Up", "Capture") ficam na tela, não na fala, quando o Veo erra. Grafias fonéticas ("Képtchur") pioraram — não usar.
- **Velocidade:** só a fala do apresentador acelera (padrão 1,2×; Looper e Vocal Riser v8 saíram em 1,1× a pedido). Música, som do plugin e demonstração ficam em 1×.
- **Sem pular quadros:** nunca acelerar um master de 30 fps. Opções: (a) render master a 30÷velocidade fps + `assemble.py`; (b) pré-acelerar takes com `setpts=(PTS-STARTPTS)/1.2,fps=30` no mesmo filtro (sem o `fps=30` o render repete/pula quadros = "trava e destrava").
- **Volume:** ganho fixo para -15 LUFS + `alimiter` (o `loudnorm` dinâmico achatava o drop). Pico < -1 dB.
- **Visual:** legendas/textos brancos com contorno preto (Montserrat Black); sem texto duplicado ao mesmo tempo; interface e logos reais (nunca inventados). Apresentador na tela enquanto fala, com o plugin como cartão abaixo do rosto (o Lucas reprovou cortes longos para telas sem ele).
- **Prova do plugin:** som do resultado sempre real (exportado do plugin). Não fabricar som de plugin. Drop pode ser a batida da música (não é saída do plugin).
- **Música de fundo:** o Lucas quer (achou silencioso sem). Antes do drop batida abafada (build), depois aberta, sempre abaixo da voz.
- **Preço:** Vocal Riser R$ 9,99 (pagamento único, Pix ou cartão). Looper Build-Up: não mostrar preço.
- **Figurino/cenário:** padrão do CLAUDE.md = moletom preto, capuz abaixado, cordões pretos, estúdio escuro. Exceções pedidas: Looper (moletom gola redonda, LED branco-gelo) e anúncio 2 do Vocal Riser (sala de casa top, blusa preta manga longa larga). Não virou padrão [A CONFIRMAR se ele quer mudar o padrão].

## 3. Estado Atual
- **KaloxSooth** (`videos/`, Hypit): pronto.
- **BankMaster 2.0** (`hyperframes/bankmaster/film/`): pronto (v11, 1,2×). Entregas antigas em 1,2× tinham o problema de pular quadros — refazer só se ele pedir.
- **Vocal Riser — Reel 1** (`hyperframes/vocalriser/film/`): pronto, v8 em 1,1× (sem pular quadros).
- **Looper / Build-Up** (`hyperframes/looper/film/`): pronto, v4 em 1,1× (só a fala acelera; música do plugin de fundo; abertura sincronizada com o build; drop real em 19,415 s do `vst-build.mp3`).
- **Vocal Riser — anúncio 1** (`hyperframes/vocalriser/anuncio/`): takes aprovados e guia de voz enviado; **parado** (faltam voz do Voice Changer e vocal cru + riser do mesmo trecho).
- **Vocal Riser — anúncio 2 "Para de desenhar automação"** (`hyperframes/vocalriser/anuncio2/film/`): **pronto, v4** (26,3 s), com a voz dele, ele na tela durante a fala, interface animada, música de fundo, legenda do post entregue. Demo ainda é a interface animada (sem gravação de tela da DAW).

## 4. Arquivos e Artefatos Relevantes
| Arquivo | Status | Descrição |
|---------|--------|-----------|
| `CLAUDE.md` | Editado | Regras de entrega do Lucas (velocidade, quadros, voz, visual) |
| `tools/transcribe.py`, `vrsync.py`, `vrfine.py`, `piclag.py`, `README.md` | Criado | Transcrição (sherpa-onnx Whisper small), sincronia da voz, conferência de quadros |
| `hyperframes/looper/film/assemble.py` | Criado | Montagem final: só a fala acelera, música 1×, ganho fixo + limiter |
| `hyperframes/looper/` (ROTEIROS, VEO-PROMPTS, NOTES, film/) | Pronto | Looper Build-Up, v4 em `film/out/looper-v4-1.1x.mp4` |
| `hyperframes/vocalriser/ROTEIRO-ANUNCIO.md`, `VEO-PROMPTS-ANUNCIO.md` | Criado | Anúncio 1 |
| `hyperframes/vocalriser/anuncio/` (NOTES, HANDOFF, assets/raw/1-3.mp4, voice guia) | Pendente | Anúncio 1, aguardando material |
| `hyperframes/vocalriser/ROTEIRO-ANUNCIO-2.md` | Criado | Roteiro + prompts do anúncio 2 (cenário sala, blusa larga) |
| `hyperframes/vocalriser/anuncio2/film/out/vocalriser-anuncio2-v4.mp4` | Pronto | Anúncio 2 final |
| `hyperframes/vocalriser/anuncio2/NOTES.md`, `HANDOFF.md` | Criado | Takes, cortes, histórico v1–v4, passo a passo |
| `hyperframes/vocalriser/film/assets/brand/` | Criado | Recortes da UI real: `ui-window-noind.png` (sem ponteiro), `chorus-off.png`, `tremolo-off.png`, `title-vocal-riser.png`, `logo-kalox.png` |
| `hyperframes/vocalriser/assets/rec/01.mp3`, `02.mp3` | Material | Risers reais exportados do plugin (1,93 s) |

## 5. Código e Configurações Críticas
Pré-acelerar takes (anúncio 2) sem trava:
```bash
ffmpeg -ss INI -t DUR -i take.mp4 -an -vf "setpts=(PTS-STARTPTS)/1.2,fps=30,format=yuv420p" -c:v libx264 -crf 14 -r 30 take-1.2x.mp4
ffmpeg -i voz-voicechanger.wav -af "atrim=start=ATRASO,asetpts=PTS-STARTPTS,atempo=1.2,aresample=48000" voz-1.2x.wav
```
Render + volume (HyperFrames pinado):
```bash
npx --yes hyperframes@0.8.210 check --json ; npx --yes hyperframes@0.8.210 snapshot --at t1,t2
npx --yes hyperframes@0.8.210 render --fps 30 -o out/raw.mp4
# I = loudness medido; ganho = -15 - I
ffmpeg -i out/raw.mp4 -c:v copy -af "volume=${G}dB,alimiter=limit=0.8:attack=1:release=50:level=false,aresample=48000" -c:a aac -b:a 192k -ar 48000 -movflags +faststart out/final.mp4
```
Conferências obrigatórias no arquivo final: `tools/vrsync.py` (voz × guia acelerado, janelas alinhadas ao início da fala), mapeamento de quadros na área do rosto (só passos 1 e repetições isoladas, nenhum pulo), `tools/transcribe.py`, ebur128.

## 6. Erros e Armadilhas Conhecidas
- Acelerar master de 30 fps com `fps=30` → descarta quadros (travadas). Usar master 30÷velocidade ou pré-acelerar com `fps=30` no mesmo filtro.
- `setpts/1.2` sem `fps=30` + `-fps_mode passthrough` → tempos arredondados, repete/pula quadros.
- `loudnorm` dinâmico achata o drop → usar ganho fixo + limiter.
- No ffmpeg: `amix` pega o início da 1ª entrada (pôr a música primeiro); loop de música dentro do grafo grande sumia → renderizar a música à parte; `atrim=a:b` posicional falhou → usar `start=`/`end=`.
- HyperFrames: vídeo com `data-start` não pode ficar dentro de bloco com `data-start`; fonte de emoji precisa de `@font-face` (`NotoColorEmoji.ttf` copiado para `assets/fonts`); `fromTo` precisa `immediateRender:false` para não vazar estado.
- Medição de sincronia com janelas começando no 0 do filme cai em pausas e dá desvio falso; medir quadros com overlay (texto/cartão) confunde — medir só a área do rosto.
- Efeitos sonoros (clique, ding) em cima de palavras somem a fala na transcrição → volumes 0,16–0,3 e fora das palavras.
- Rede: Google Drive bloqueado (download e conector derrubam com arquivos grandes); upload via chat tem limite (~25 MB); usar MP4 1080p curto ou GitHub.
- Veo: olhos arregalados quando o prompt pede "sobrancelhas levantadas/impressionado"; celular aparece na mão se a fala cita celular (proibir no prompt); corta a última palavra às vezes.

## 7. Próximos Passos
- [ ] Anúncio 2: se o Lucas mandar gravação de tela da DAW com som, trocar a interface animada pela gravação (cena 2,45–9,08 s e 12,2–13,79 s).
- [ ] Anúncio 1: receber voz do Voice Changer + vocal cru e riser do mesmo trecho; montar conforme `anuncio/HANDOFF.md`.
- [ ] Opcional: refazer o arquivo final do BankMaster sem pular quadros (só se ele pedir).

## 8. Informações Pendentes
- Velocidade padrão: 1,2× (CLAUDE.md) ou 1,1× (usado no Looper/Vocal Riser)? Não confirmado.
- Figurino/cenário novo (sala + blusa larga) vira padrão? Não confirmado.

---

## 🛠️ Skills e ferramentas usadas
- **Skills:** `hyperframes` (composições HTML/GSAP renderizadas em vídeo — todos os projetos em `hyperframes/`), `hypit` (KaloxSooth, `videos/`), `anthropic-skills:context-compressor-handoff` (este arquivo). [A CONFIRMAR: `hyperframes-cli` foi consultado via `npx hyperframes docs`, não como skill.]
- **Ferramentas:** HyperFrames CLI 0.8.210 (pinado), ffmpeg, Python (numpy, Pillow, sherpa-onnx Whisper small + Silero VAD), Gemini/Nano Banana e Veo 3 (lado do Lucas), ElevenLabs Voice Changer (lado do Lucas).

## 💬 Preferências do Usuário (relevantes para o trabalho)
- Português do Brasil, direto, sem enrolação; quer resultado pronto e rápido ("acelera aí, tenho que postar").
- Odeia: tremida de câmera, flash branco no começo, travadas, voz que não é a dele, texto repetido, vídeo silencioso, imagens "bugadas"/paradas do plugin.
- Gosta: ele na tela falando, plugin animado de verdade (botão girando, FX piscando), animações de entrada/saída, efeitos de atenção discretos, música do plugin de fundo, drop no corte.
- Sempre conferir sincronia no arquivo final e dizer os números; entregar também a legenda do post (termina com "Comenta RISER/DROP que eu te mando o link"; em anúncio pago, "Toca em Saiba mais").

---

> **Instrução para o próximo chat:** Este arquivo contém o contexto compactado de um chat anterior. Use-o como base para continuar o trabalho. Não peça ao usuário para repetir informações que já estão aqui. Comece confirmando brevemente que entendeu o contexto e pergunte por onde o usuário quer continuar.
