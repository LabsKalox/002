# BankMaster 2.0 — teaser v1

- Entrega: `out/bankmaster-teaser-v9-final.mp4` (21,35 s, 1080×1920, -15,7 LUFS, pico -1,3 dB).
- Material: 3 clipes do Veo 3 (`assets/raw/clip-c|b|a.mp4`). No clip-b, o "Espera!" repetido
  (src 5,2–6,65 s) foi cortado.
- Música: `assets/audio/beat-*.wav`, gerados por `tools-beat.py` (trap 140 bpm sintetizado). A versão
  abafada toca no gancho ("master fraca") e a cheia a partir da revelação.
- O seletor de gênero e o "MASTERIZANDO..." são tipografia animada, não a interface do plugin.
  Quando chegar a gravação de tela do BankMaster, ela entra depois de "Olha isso aqui" (7,75 s).
- O clipe final ainda diz "te aviso primeiro" (gerado antes da troca para "envio na sua DM").
- Render: `npx hyperframes render --output out/bankmaster-teaser-v1.mp4`, depois
  `ffmpeg -i ... -c:v copy -af loudnorm=I=-15:TP=-1.5:LRA=11` para o arquivo final.
- O GSAP é local (`assets/gsap.min.js`) porque a rede do ambiente bloqueia o cdn.jsdelivr.net.

## v2 — interface e logos reais
- Fonte: `assets/brand/promo-original.png` (arte enviada pelo usuário, 1600×900).
  Recortes: `ui-window.png` (janela do plugin), `logo-bankmaster-alpha.png` e `logo-kalox-alpha.png`
  (fundo escuro convertido em transparência), `ui-bg.png` (brilho laranja desfocado para o fundo vertical).
- 7,85 s: o logo real substitui o título digitado. 9,55–14,25 s: cena da interface. Zoom no seletor de
  preset ("Modern Punch") com destaque laranja em "escolhe o gênero"; depois zoom no medidor OUTPUT em "e espera!".
- 21,3–22,2 s: cartela final com o logo BankMaster 2.0 + Kalox Audio + "EM BREVE".
- A arte diz "AVAILABLE NOW" (com uma letra defeituosa); esse trecho não foi usado. Falta confirmar com o
  usuário se é "EM BREVE" ou "JÁ DISPONÍVEL".

## v3
- Gêneros: só Afro House, Deep House e Indie Dance (para em AFRO HOUSE).
- Música trocada por um groove de house a 122 bpm (`tools-beat.py`).

## v4 — voz do usuário (clone ElevenLabs)
- Voz: `assets/voice/voz-elevenlabs.mp3` (17,9 s). Os clipes do Veo foram reajustados com
  `tools-sync.py` (DTW entre a voz nova e a voz original do Veo, peças de 6 quadros, velocidade entre 0,5× e 1,8×;
  acima disso vira corte seco). Saídas: `assets/synced/s1|s2|s3.mp4` (sem áudio) + `.pieces.json`.
- s1 recebeu um ajuste fino no início (`-0.19:0.7:1.1`) porque a boca adiantava 190 ms.
- Sincronia medida (envelope da voz vs. voz original reajustada): entre -40 e +20 ms nas partes visíveis.
- Cortes secos do retime com troca de zoom (jump cut): 3,6 / 5,2 / 5,8 / 14,7 / 15,3 / 16,3 s.
- Duração 18,7 s; -14,9 LUFS.

## v5 — correção de sincronia
- Bug da v4: os clipes retimados perdiam quadros (filtros por peça com fps/trim arredondando): s1 6,43 s em vez de
  6,53; s2 5,97 em vez de 6,13; s3 5,70 em vez de 6,00. A imagem escorregava até 8 quadros (≈0,27 s) no final.
- Correção: `tools-render-pieces.py` gera cada quadro de saída a partir do quadro de origem mais próximo do
  tempo mapeado (contagem exata: 196/184/180). `tools-sync.py` continua gerando o mapa (`.pieces.json`).
- Verificado no arquivo final: imagem vs. clipe sincronizado com 0 quadro de diferença em janelas de 1 s.

## v6 — Voice Changer (versão atual)
- Abandonado o retime da imagem (v4/v5): os cortes e as acelerações ficavam visíveis.
- A fala original do Veo, no tempo do corte (`assets/voice/veo-fala-original-para-voice-changer.wav`, 22,2 s),
  passou pelo Voice Changer do ElevenLabs com o clone do usuário → `assets/voice/voz-voicechanger.mp3`.
  O ElevenLabs adicionou 1,42 s de silêncio no início; cortado com `data-media-start="1.42"`.
- A imagem volta a ser a original da v3 (clipes do Veo sem retime, agora mudos). Verificado: voz no arquivo
  final vs. fala original do Veo entre -5 e +5 ms.
- A fala final segue a do Veo: "comenta MASTER que eu te aviso primeiro" (legenda igual).
- `assets/synced/` e `tools-sync.py`/`tools-render-pieces.py` ficam como ferramenta para quando não houver a
  fala original (ex.: uma voz gravada do zero).

## v7 — áudio editado pelo usuário (`assets/audio/2213.mp3`)
- É a voz do Voice Changer com 0,85 s a menos na pausa de "e ela continua… fraca" (corte no 5,355 s do arquivo).
- A imagem recebeu o mesmo corte: `hook` vai até 3,88 s e `hook-b` retoma o clip-c em 4,73 s (jump cut com troca
  de zoom). Tudo depois do corte foi puxado 0,85 s para trás. Voz com `data-media-start="1.47"`.
- Sincronia no arquivo final (voz vs. fala original do Veo com o mesmo corte): de 0 a +10 ms; -20 ms no fim.
- Duração 21,35 s; -15,8 LUFS.

## v8 — final da fala no tempo da boca
- O `2213.mp3` também tinha "Tá chegando" (+110 ms) e "te aviso primeiro" alterados, fora do tempo da boca.
- Agora: `2213.mp3` até 15,5 s do filme (pausa antes de "Tá chegando"); dali até o fim, `voz-voicechanger.mp3`
  (`data-media-start="17.77"`, mesmo volume medido).
- Verificado em janelas de 0,6 s no arquivo final: de -20 a +15 ms no vídeo todo.

## v9 — só a voz do usuário (`2213.mp3`), imagem ajustada a ela
- Pedido: usar apenas o arquivo do usuário, sem emendas do Voice Changer.
- Erro da v7/v8: a pausa removida no `2213.mp3` fica entre "alta?" e "e ela continua" (≈3,3 s do filme), não no meio
  de "continua" (o corte de imagem em 3,88 s tirou a boca falando).
- Agora: `tools-sync.py` (MAXRATE=2.6) + `tools-render-pieces.py` geram `assets/synced/hook-2213.mp4` e
  `assets/synced/cta-2213.mp4`. Gancho: velocidade 0,95–1,05× e um corte de 0,83 s em 3,4 s (no silêncio).
  Final: um corte de 0,5 s em 19,0 s (dentro de "te aviso", onde a voz adianta 0,5 s); a alternativa sem corte errava até 120–200 ms.
  Troca de zoom em cada corte.
- Medido: boca vs. voz entre -15 e +15 ms (janelas de 0,5 s); imagem final vs. clipes ajustados: 0 quadro até 20,2 s.
