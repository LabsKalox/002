# Passagem de bastão — Reel/anúncio do Vocal Riser (para o agente local)

Leia antes: `/CLAUDE.md` (regras de entrega do Lucas), `../ROTEIRO-ANUNCIO.md` (roteiro segundo a segundo),
`NOTES.md` (takes e cortes), `../VEO-PROMPTS-ANUNCIO.md`. Modelos prontos: `hyperframes/looper/film/` (projeto
HyperFrames com plugin animado, legendas, entradas/saídas) e `hyperframes/looper/film/assemble.py` (montagem final:
só a fala acelera, música/plugin em 1×, sem pular quadros).

## Já feito
- 3 takes do Veo aprovados em `assets/raw/1.mp4`, `2.mp4`, `3.mp4` (falas certas, roupa certa, mãos vazias).
- Fala para o Voice Changer: `assets/voice/anuncio-fala-para-voice-changer.wav` (18,7 s) =
  1[0,90–6,65] + 2[0,95–7,50] + 3[1,05–7,45]. Já foi enviada ao Lucas.
- Interface real: `hyperframes/vocalriser/assets/brand/vocal-riser-ui.png` e recortes em
  `hyperframes/vocalriser/film/assets/brand/` (ui-window.png, ui-window-noind.png, chorus-off.png, tremolo-off.png,
  title-vocal-riser.png, logo-kalox.png). Risers exportados: `hyperframes/vocalriser/assets/rec/01.mp3`, `02.mp3`.

## Falta (material do Lucas, no computador dele)
1. Voz do Voice Changer (ElevenLabs, clone dele) a partir do WAV acima — devolvida sem edição.
2. Vocal cru + o riser que saiu dele (mesmo trecho, WAV) para o antes/depois (2–7 s do roteiro).
3. Gravação de tela clicando no plugin (opcional; sem ela, animar a interface real como no Looper).

## Como montar
1. Projeto HyperFrames novo em `hyperframes/vocalriser/anuncio/film/` (copiar a estrutura do Looper).
2. 0–2 s: riser subindo + drop com a tela do plugin; 2–4 s "ANTES: vocal cru"; 4–7 s "DEPOIS: 1 clique".
   Texto fixo desde o 1º quadro: "RISER DE VOCAL EM 1 CLIQUE" + selos "R$ 9,99" e "MAC E WINDOWS".
3. Depois os 3 takes com a voz dele (medir o atraso inicial do Voice Changer e cortar só isso), legendas brancas com
   contorno preto, sem duplicar o que os selos já dizem; textos de apoio do roteiro (Reverse 1 a 4 compassos /
   Chorus · Tremolo · Phone / Pix ou cartão / VST3 · AU / DAWs / Compra no celular → link no e-mail → baixa no PC).
4. Cartela: "Toca em SAIBA MAIS · Link na bio · kaloxproduction.com".
5. Entrega em 1,2× só na fala (demo e riser em 1×), via assemble.py adaptado; conferir sincronia no arquivo final,
   mapeamento de quadros, transcrição, -15 LUFS e pico < -1 dB.
