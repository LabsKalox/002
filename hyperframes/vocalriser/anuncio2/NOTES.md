# Vocal Riser — anúncio 2 ("Para de desenhar automação de riser"), roteiro em `../ROTEIRO-ANUNCIO-2.md`

## Takes (16/11), 24 fps, 7,93 s, sala de casa top, blusa preta manga longa larga, mãos vazias
- `assets/raw/u1.mp4` = Take A: "Para de desenhar automação de riser. Joga o vocal no Vocal Riser." (fala 1,40–6,10)
- `assets/raw/u2.mp4` = Take B: "Ele faz o reverse de um a quatro compassos, com chorus, tremolo e phone." (1,40–6,40)
- `assets/raw/u4.mp4` = Take C (escolhido): "Dá pra ajustar tudo depois. Um botão só, riser pronto pro drop." (1,25–6,30)
- `assets/raw/u6.mp4` = Take C alternativo (pausa/tropeço entre "riser" e "pronto"; não usado)
- Fundo varia um pouco entre os takes (Veo), mas é a mesma sala/estilo.

## Preço / Mac-Windows / celular
Reaproveitados do anúncio 1 (`../anuncio/assets/raw/2.mp4` e `3.mp4`) só como **voz em off** sobre as artes (R$ 9,99,
ícones Mac/Windows, celular → e-mail → PC, botão SAIBA MAIS): o rosto não aparece, porque esses takes são no estúdio
verde com moletom e não combinam com a sala.

## Fala para o Voice Changer
`assets/voice/anuncio2-fala-para-voice-changer.wav` (29,5 s) = u1[1,10–6,40] + u2[1,10–6,70] + u4[0,95–6,60] +
anuncio/2[0,95–7,50] + anuncio/3[1,05–7,45]. A 1,2× a fala dá ~24,6 s (o roteiro pedia 18–20 s).

## Edição v1 (prévia) — `film/`
- Linha do tempo já é a entregue: takes acelerados 1,2× antes (vídeo `setpts/1.2`, todos os quadros, 28,8 fps) e voz
  com `atempo 1.2`; riser/batida/efeitos em 1×. Render único a 30 fps (sem pular quadros: a fonte tem menos quadros
  que a saída).
- **Voz provisória** = fala original do Veo (`film/assets/voice/voz-temp-veo-1.2x.wav`). Trocar pela do Voice Changer:
  medir o atraso inicial contra o guia (`tools/vrsync.py`), cortar, aplicar `atempo=1.2`, mesmo nome de clipe.
- **Sem gravação de tela ainda**: a demo usa a interface real animada (botão gira, CHORUS/TREMOLO acendem, PHONE
  destacado) e o riser real exportado do plugin (`02.mp3`). O drop é a batida da casa (`beat.wav`) + impacto.
- Cenas: 0–2,45 Take A + PARA DE DESENHAR AUTOMAÇÃO; 2,45–9,08 plugin (selo, REVERSE, CHORUS·TREMOLO·PHONE);
  9,08–12,2 Take C (AJUSTA TUDO DEPOIS, UM BOTÃO SÓ); 12,2–13,79 riser → drop; 13,79 R$ 9,99/PAGAMENTO ÚNICO/PIX OU
  CARTÃO; 17,69 MAC/WINDOWS + DAWs; 19,25 celular → e-mail → PC; 23,5 TOCA EM SAIBA MAIS até 26,3.
- Conferido: voz × fala original 0 ms; transcrição completa; -15,5 LUFS, pico -1,6 dB. Saída `film/out/vocalriser-anuncio2-v1.mp4`.

## Edição v2 — com a voz do Lucas e ele na tela enquanto fala
- O Lucas achou a v1 ruim (voz do Veo, muito tempo de tela sem ele). Na v2:
  - voz: `assets/voice/anuncio2-voz-voicechanger.wav` (Voice Changer), atraso constante de 25 ms cortado, `atempo 1.2`
    → `film/assets/voice/voz-lucas-1.2x.wav`;
  - ele fica na tela em toda a fala (Take A 0–4,42, Take B 4,42–9,08, Take C 9,08–13,79), com o plugin como cartão
    abaixo do rosto e os textos no topo; preço/Mac-Windows/celular sobre a sala desfocada (`room-bg.png`);
  - riser sob "riser pronto pro drop" em 0,4 e batida pós-drop em 0,09 (antes cobriam a fala).
- Conferido no arquivo final: voz × fala original 0 ms (39/39 janelas em ±40 ms); imagem dentro de 1 quadro nos 3
  takes; transcrição completa; -15,3 LUFS, pico -1,8 dB. Saída: `film/out/vocalriser-anuncio2-v2.mp4` (26,3 s).
