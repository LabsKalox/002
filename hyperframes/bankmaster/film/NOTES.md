# BankMaster 2.0 — teaser v1

- Entrega: `out/bankmaster-teaser-v1-final.mp4` (21,9 s, 1080×1920, -15,7 LUFS, pico -1,3 dB).
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
