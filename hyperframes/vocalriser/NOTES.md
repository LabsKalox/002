# Vocal Riser — notas de produção

- Takes do Veo (`assets/raw/`): 00 = Take 1 (usado), 01 = Take 1 alternativo (repete "de um pedaço", descartado),
  02 = Take 2, 03 = Take 3. Rosto, roupa e fundo verde conferidos.
- Fala para o Voice Changer, no tempo da edição: `assets/voice/vr-fala-para-voice-changer.wav` (21,25 s)
  = 00[0–6,4] + 02[0–7,45] + 03[0–7,4].
- Estrutura planejada: abertura com o plugin gerando o riser (2–3 s, gravação de tela com som) → Take 1 →
  Take 2 (close no plugin) → Take 3 → cartela. Falta a gravação de tela do plugin.

## Edição v1 (HyperFrames, `film/`)
- Voz: `vr-voz-voicechanger-v2.mp3` (Voice Changer, 2ª versão do usuário). Sai 135 ms adiantada em relação à
  fala do Veo, constante do início ao fim → entra em 2,635 s do filme (sem cortes). Medido no arquivo final:
  0 ms (±10–40 ms nas sílabas; desvios só nas pausas, onde só toca a batida).
- 0–2,5 s: **provisório** (interface + aviso). Trocar pela gravação de tela do plugin gerando o riser, com som.
- Close na interface real (11,2–15,1 s): destaque em REVERSE | 1 BAR, depois CHORUS e TREMOLO; sem legenda
  nesse trecho para não duplicar o texto da interface.
- Final "que eu te mando": o próprio Take 3 do Veo termina em "mand" (o "o" sai quase mudo); na v2 da voz a
  transcrição automática não reconhece bem esse trecho — conferir no ouvido.
- Saídas: `out/vocalriser-v1-final.mp4` (1×, -15 LUFS, pico -1,3 dB) e `out/vocalriser-v1-1.2x.mp4` (21,7 s).
