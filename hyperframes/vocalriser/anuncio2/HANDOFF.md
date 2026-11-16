# Passagem de bastão — anúncio 2 do Vocal Riser ("Para de desenhar automação de riser")

Ler antes: `/CLAUDE.md` (regras do Lucas), `../ROTEIRO-ANUNCIO-2.md` (roteiro segundo a segundo), `NOTES.md` (takes e
cortes), `/tools/README.md` (ferramentas de conferência). Modelo de edição: `hyperframes/looper/film/` (HyperFrames:
plugin animado, legendas, entradas/saídas) e `hyperframes/looper/film/assemble.py` (só a fala acelera; demo/música 1×;
sem pular quadros; música renderizada à parte; ganho fixo para -15 LUFS + limiter).

## Material
- Takes (já no repo): `assets/raw/u1.mp4` (A), `u2.mp4` (B), `u4.mp4` (C). Preço/Mac-Windows e celular/Saiba mais:
  `../anuncio/assets/raw/2.mp4` e `3.mp4`, só como voz em off (o rosto não aparece; outro cenário).
- Guia da fala: `assets/voice/anuncio2-fala-para-voice-changer.wav` (29,5 s) = u1[1,10–6,40] + u2[1,10–6,70] +
  u4[0,95–6,60] + anuncio/2[0,95–7,50] + anuncio/3[1,05–7,45].
- Do Lucas (no computador dele): a voz do Voice Changer (feita a partir do guia) e a gravação de tela com som
  (vocal na DAW → abre o plugin → 1 clique → riser entrando no drop).
- Interface real: `hyperframes/vocalriser/film/assets/brand/` (ui-window.png, ui-window-noind.png, chorus-off.png,
  tremolo-off.png, title-vocal-riser.png, logo-kalox.png).

## Montagem (tempos do arquivo final, fala a 1,2×)
1. 0–2 s: Take A (rosto) desde o 1º quadro, sem flash; texto PARA DE DESENHAR AUTOMAÇÃO; som do riser da gravação
   subindo por baixo.
2. "Joga o vocal no Vocal Riser e…": corta para a gravação da DAW abrindo o plugin; selo VOCAL RISER; voz em off.
3. "…ele faz o reverse…": um clique na gravação; textos REVERSE 1 A 4 COMPASSOS e CHORUS · TREMOLO · PHONE.
4. "Um botão só. Riser pronto pro drop.": o riser entra no drop (som da gravação em 1×); texto UM BOTÃO SÓ.
5. "Nove e noventa e nove…": arte R$ 9,99 + PAGAMENTO ÚNICO; depois ícones Mac e Windows (voz em off).
6. "Compra pelo celular…": ícones CELULAR → E-MAIL → PC; "Toca em Saiba mais": botão SAIBA MAIS + dedo apontando.
- Legendas brancas com contorno preto (Montserrat Black), sem repetir o que um texto/selo já diz no mesmo instante.
- Voz: medir com `tools/vrsync.py` o atraso inicial do Voice Changer contra o guia e cortar só isso. Nos trechos com
  rosto, a voz tem que bater com a boca (medir no arquivo final, janelas alinhadas ao início da fala).
- Entrega: vertical 1080×1920, 30 fps, -15/-16 LUFS, pico < -1 dB; conferir transcrição, sincronia e mapeamento de
  quadros. Duração esperada ~24–25 s (pedido era 18–20 s; para encurtar, tirar "Dá pra ajustar tudo depois" da fala).
