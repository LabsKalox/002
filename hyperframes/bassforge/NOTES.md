# BassForge — anúncio (plugin MIDI de linhas de baixo)

- Takes Veo (24 fps): take1 "Escuta essa linha de baixo. Esse plugin gerou ela com um clique." | take2 "Afro House. Deep House. Tech House." |
  take3 "Gostou? Arrasta pra sua DAW." | take4 "BassForge. Dezoito e noventa, pagamento único. Só pra Mac. Toca em Saiba mais." (manga longa ok nos 4).
- `build_assets.py`: corta nas pausas (imagem e áudio no mesmo ponto, 1,25x: 1 quadro de 24 fps = 1 de 30 fps), caudas de silêncio
  (ele calado) para o baixo tocar sozinho (áudio do guia mudo na cauda), 3 quadros de preparação na imagem (só imagem).
- Voz: guia → Voice Changer (`assets/voice/bassforge-voz-voicechanger.wav`, +20..+40 ms, global +30) → `atrim=0.03`, `atempo=1.25`;
  entra em 0,06 s no filme (= preparação 0,1 s − 40 ms de adiantamento; Veo: áudio 40–80 ms atrás da boca nesses takes).
- Layout (faixa segura da Meta, rosto em tela cheia sem bordas): rosto sobe 340 px (olhos y≈390, queixo ≤ 776), legenda em y 795,
  plugin em x 65–1015, y 865–1250. Abaixo de 1380 degradê para o preto (área da UI da Meta).
- Interface real (prints do Lucas): `film/assets/ui/` — `stage-base.png` (print sem as 10 notas e sem o clip da DAW), `note*.png`,
  `clip.png`, `gen-btn.png`, `drag-btn.png`, `menu-base.png` (menu sem o ✓), `wordmark-a.png` (logo real com fundo transparente).
  Câmera passeia pela interface: piano roll com playhead (120 bpm, 2 compassos = 4 s) → GENERATE apertado → notas nascem →
  menu de estilos (Afro → Deep → Tech) → DRAG TO DAW (clip voa até a pista) → logo, R$ 18,90, macOS, SAIBA MAIS.
- `make_index.py` gera `film/index.html` a partir de `assets/timeline.json`.
- Bateria 120 bpm sintetizada SEM baixo (`tools-drums.py`). O baixo do vídeo tem que ser o do BassForge (pendente: WAVs do Lucas).
- v1 (sem baixo): 16,53 s, -15,5 LUFS, pico -1,8 dBFS; voz +61 ms (esperado +60); sem quadros repetidos; sem flash.
  Transcrição: ok, mas conferir no ouvido "Tech House" (Whisper: "Deck House"), "DAW" e "BassForge" ("Basford").
