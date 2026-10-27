# Troca de estúdio do A-roll (Veo 3)

Objetivo: o mesmo personagem, a mesma fala e os mesmos gestos, num estúdio de produção musical
de alto padrão. O caminho em duas etapas mantém o rosto: primeiro editar o quadro inicial, depois
gerar o vídeo a partir dele.

Arquivos de apoio: `assets/frame-inicial.png` (quadro 0 do vídeo atual, 1080×1920) e
`assets/frame-final-mesa.png` (giro para a mesa, 7,6 s).

---

## Etapa 1 — Editar o quadro inicial (Gemini / Nano Banana, GPT Image, FLUX)

Versão escolhida: **estúdio todo preto, premium e futurista**. A primeira versão, com madeira e
luz âmbar, foi descartada pelo usuário.

Ponto técnico: moletom preto sobre fundo preto faz o personagem "sumir". Por isso o prompt pede
uma luz de recorte (rim light) no cabelo e nos ombros e um fundo levemente mais claro atrás da cabeça.

Envie `frame-inicial.png` e use (troque `[ACENTO]` por uma das cores abaixo):

```
Edit this photo. Keep the man exactly as he is: same face, same expression, same hair,
same black hoodie, same pose, same camera distance and the same vertical selfie framing.
Change only the place around him.

He now sits in an all-black, futuristic, high-end music production studio at night.
Behind him: matte black ribbed acoustic wall panels, a floating black desk with a glossy
black surface, a large ultra-wide curved monitor glowing softly out of focus, sleek black
studio monitors, and thin recessed linear LED light lines running along the walls and
ceiling in [ACENTO]. Minimal, clean, expensive, like a flagship studio. No clutter.
His seat is a black leather studio chair.

Palette: deep matte black and graphite, glossy black reflections, with [ACENTO] light lines
as the only color. The light on his face matches this room: a soft cool key light from the
front-left, and a clear [ACENTO] rim light on his hair and shoulders that separates his black
hoodie from the dark background. The wall directly behind his head is slightly lit so his
silhouette reads clearly.

Natural shallow depth of field from a phone front camera. Photorealistic, no text, no logos.
```

| Opção | `[ACENTO]` | Efeito |
|---|---|---|
| **A (recomendada)** | `icy light blue` | Combina com a interface azul-clara do KaloxSooth: o vídeo e o plugin parecem a mesma marca |
| B | `soft cool white` | Minimalista, "Apple": o mais premium e neutro |
| C | `deep red` | Cyberpunk, combina com as ondas vermelhas da DAW: mais agressivo |

Confira antes de seguir: o rosto continua idêntico? A mão e o moletom estão iguais? O cenário
está desfocado o suficiente para o rosto continuar sendo o centro? Se o rosto mudou, gere de novo.

---

## Etapa 2 — Gerar o vídeo (Veo 3 → Frames to Video, 9:16, com áudio)

Quadro inicial: a imagem aprovada da Etapa 1.

```
Vertical selfie video, handheld phone front camera, natural and lightly moving.
A Brazilian music producer in his early thirties, black hoodie, sits in his all-black
futuristic music studio at night (matte black ribbed acoustic panels, floating glossy black
desk, curved monitor glow, thin recessed [ACENTO] LED light lines, [ACENTO] rim light on him).

He looks straight into the lens with a friendly, slightly mischievous energy, like he is
about to show a friend something impressive.

0-1s: he smiles and waves the viewer closer with his thumb, a casual "come here" gesture.
1-5s: he speaks warmly and confidently, relaxed shoulders, small head nods on the key words.
5-6.5s: he points down toward the bottom of the frame twice, excited.
6.5-8s: he turns the phone away from his face and the camera swings to his desk,
revealing the black desk and a large curved monitor showing a music production session.

Dialogue, in Brazilian Portuguese, casual and energetic male voice:
"Vem cá que eu vou te mostrar o que o meu plugin novo faz nessa mix ardida. Olha isso aqui, olha isso aqui!"

Audio: only his voice and quiet room tone. No music.
No subtitles, no captions, no on-screen text.
```

Dicas:
- Gere de 2 a 4 versões e escolha pela boca sincronizada e pela naturalidade dos gestos.
- Se o Veo colocar legenda na imagem, gere de novo; o "No subtitles" costuma resolver.
- Se a voz mudar muito em relação à versão atual, tudo bem: as legendas e a edição se ajustam à nova fala.

---

## Alternativa sem o Veo

Higgsfield (conectado nesta sessão): Seedance 2.0 ou FLUX 3 Video aceitam quadro inicial e geram
áudio. Hoje a conta tem 0 créditos (plano grátis). Exige compra de créditos e aprovação de custo antes.
