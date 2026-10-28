# BankMaster 2.0 — teaser v1

- Entrega: `out/bankmaster-teaser-v3-final.mp4` (22,2 s, 1080×1920, -15,7 LUFS, pico -1,3 dB).
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
