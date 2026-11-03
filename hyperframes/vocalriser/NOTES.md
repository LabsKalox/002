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

## Edição v2 (final, aprovada pelo usuário)
- Sem música de fundo (só voz + whoosh/impacto nas viradas); aviso "provisório" removido. A abertura (0–2,5 s)
  fica com a interface real do plugin.
- Sincronia medida no arquivo final: 0 ms (32 de 34 janelas dentro de ±40 ms; as 2 fora são pausa/efeito).
- Saídas: `out/vocalriser-v2-final.mp4` (1×) e `out/vocalriser-v2-1.2x.mp4` (21,7 s, -15,8 LUFS, pico -1,4 dB).

## Edição v3 (abertura com o riser real)
- Material do usuário (`assets/rec/`): 3 gravações de tela do Ableton sem áudio (960 px, 12 fps) + 2 risers
  exportados do plugin (`01.mp3`, `02.mp3`, 1,93 s cada = 1 compasso).
- Abertura: janela do Vocal Riser recortada da gravação das 19h20 (`film/assets/rec/intro-plugin.mp4`),
  ampliada sobre fundo desfocado da própria tela, com push-in que acelera junto com o riser 02.
  O riser termina exatamente no corte para o Take 1.
- O render começa 1,1 s depois do início do riser (cabeça silenciosa cortada no ffmpeg); a sincronia foi medida
  com a fala do Veo deslocada para 1,4 s: 0 ms (33/34 janelas em ±40 ms; a de fora é o riser antes da fala).
- Saídas: `out/vocalriser-v3-final.mp4` (1×, 25 s) e `out/vocalriser-v3-1.2x.mp4` (20,8 s, -16,1 LUFS, pico -1,4 dB).

## Edição v4 (pedido do usuário: plugin menor, estático e inteiro)
- Abertura: imagem real da interface inteira, a 72% do tamanho, parada (sem zoom), com o riser 02 por baixo.
  A gravação de tela saiu da abertura.
- Meio do vídeo (11,2–15,1 s): a interface inteira a 58% por cima do Take 2, abaixo do rosto (o usuário não gostou
  do zoom cortando o plugin pela metade); os contornos verdes seguem a fala (REVERSE | 1 BAR, CHORUS, TREMOLO).
- Sincronia no arquivo final: 0 ms (33/34 janelas em ±40 ms; a de fora é o riser antes da fala).
- Saídas: `out/vocalriser-v4-*` (substituídas pela v5) (20,8 s, -16,1 LUFS, pico -1,4 dB).
- v5: caixa "É o Vocal Riser" desceu 150 px (top 1230), abaixo do queixo. Saídas `out/vocalriser-v5-final.mp4` e
  `out/vocalriser-v5-1.2x.mp4`; sincronia no final: 0 ms (33/34 janelas em ±40 ms).

## Edição v6 (animação no plugin + sons de atenção)
- Plugin: ponteiro do botão separado da imagem (`ui-window-noind.png` + ponteiro em CSS) e girando até ~58°
  (1 BAR, como na gravação real); CHORUS/TREMOLO com versão apagada (`chorus-off.png`, `tremolo-off.png`) que
  acende piscando quando ele fala o nome; brilho da onda pulsando em 1/16 (abertura) e 1/8 (meio).
- SFX sintetizados no ffmpeg (`assets/sfx/pop|click|tick|ding.wav`) + hit/whoosh: pop no punch-in, impacto no
  nome, ticks no botão, cliques nos FX, impacto + tremida no "drop" (20,2 s), ding no "Comenta RISER", impacto na
  cartela. Volumes baixos (0,16–0,3) para não mascarar a voz (com 0,4–0,45 a transcrição perdeu "tremolo").
- Sincronia no final: 0 ms; as janelas fora de ±40 ms caem nos SFX (conferido sílaba por sílaba).
- Saídas: `out/vocalriser-v6-final.mp4` e `out/vocalriser-v6-1.2x.mp4` (20,8 s, -16,1 LUFS, pico -1,4 dB).

## Edição v7
- Tirada a tremida de câmera no "drop" (o usuário não gostou); o impacto sonoro continua.
- Entrega em **1,1×** a pedido do usuário ("pra ver se não fica tão acelerado"): `out/vocalriser-v7-1.1x.mp4`
  (22,6 s, -16,0 LUFS, pico -1,4 dB). O padrão do CLAUDE.md segue 1,2× até ele confirmar a mudança.
- Sincronia no final: 0 ms (janelas fora de ±40 ms só nos SFX).

## Edição v8 (correção das "travadas")
- Causa: o 1,1× era feito a partir do master de 30 fps; `setpts/1.1,fps=30` descartava 1 quadro a cada 10 (no 1,2×,
  1 a cada 5 — afetou também as entregas anteriores, inclusive BankMaster). Medido: o render 1× estava correto
  (cada quadro = o quadro certo do Veo, ≤ 1 quadro de diferença).
- Correção: master renderizado a `--fps 300/11` (= 30 ÷ 1,1), corte de 30 quadros (1,1 s) e aceleração 1,1× →
  30 fps exatos, 1 quadro do master por quadro de saída (conferido em 240 quadros: nenhum descartado).
- Sincronia da voz: 0 ms; imagem ≤ 1 quadro do esperado. Saídas: `out/vocalriser-v8-master.mp4` (27,27 fps) e
  `out/vocalriser-v8-1.1x.mp4` (22,7 s, -15,8 LUFS, pico -1,4 dB).
