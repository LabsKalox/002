# Kit de variações de fundo (mesma gravação, só o fundo muda)

Tudo igual ao vídeo aprovado: mesma pose sentado, mesma câmera selfie, mesmo enquadramento, mesmo moletom
todo preto com capuz abaixado e cordões pretos, mesmas falas e gestos. Muda **apenas o fundo**, para a grade do
perfil não ficar repetida. Gire entre as opções a cada vídeo (F1 → F2 → F3 → F4 → F5 → F1…).

## Passo 1 — Quadro inicial com o fundo novo (Gemini / Nano Banana)
Envie `assets/frame-inicial-estudio-preto.png` e cole o texto base + o fundo escolhido:

```
Edite esta foto mudando SOMENTE o fundo atrás dele. Mantenha exatamente igual: o rosto, o cabelo, a expressão, a pose, a cadeira, o enquadramento, o ângulo e a distância da câmera, e o moletom todo preto com o capuz abaixado e cordões pretos. Não mude a posição dele nem o tamanho dele na imagem. A luz no rosto pode se ajustar para combinar com o novo fundo. Fotorrealista, sem texto, sem logos. Novo fundo:
```

## Passo 2 — Takes no Veo
Use os prompts de `VEO-PROMPTS-V2.md` com o quadro inicial novo (Frames to Video, 9:16, com áudio).
Troque **apenas** o trecho entre parênteses do estúdio (`Mesmo estúdio todo preto e futurista à noite (...)`)
pela linha "Para o Veo" do fundo escolhido. Nada mais muda.

---

## F1 — Parede de LED laranja (cor da marca)
Fundo (Gemini):
```
um estúdio de música escuro com a parede de trás em painéis pretos ripados atravessados por linhas de LED verticais laranja âmbar, formando um padrão geométrico; monitores de estúdio desfocados nas laterais.
```
Para o Veo: `Estúdio de música escuro à noite (parede de painéis pretos ripados com linhas de LED verticais laranja âmbar, monitores de estúdio desfocados nas laterais)`

## F2 — Madeira escura e luz quente
Fundo (Gemini):
```
um estúdio de música premium com difusores acústicos de madeira escura, abajures de luz âmbar quente, uma mesa de mixagem grande desfocada e uma planta escura no canto.
```
Para o Veo: `Estúdio de música premium à noite (difusores de madeira escura, abajures de luz âmbar quente, mesa de mixagem grande desfocada, planta escura no canto)`

## F3 — Parede de sintetizadores com luz roxa
Fundo (Gemini):
```
um estúdio de música escuro com uma prateleira cheia de sintetizadores e drum machines com botões iluminados, cabos coloridos, e uma luz de fundo roxa e azul suave.
```
Para o Veo: `Estúdio de música escuro à noite (prateleira cheia de sintetizadores com botões iluminados, cabos coloridos, luz de fundo roxa e azul suave)`

## F4 — Tijolinho preto e neon branco
Fundo (Gemini):
```
um estúdio de música estilo loft com parede de tijolinho pintado de preto, um letreiro de neon branco em forma de onda sonora (sem letras), caixas de som pretas e luz baixa.
```
Para o Veo: `Estúdio de música estilo loft à noite (parede de tijolinho preto, letreiro de neon branco em forma de onda sonora, sem letras, caixas de som pretas, luz baixa)`

## F5 — Vidro da sala de gravação ao fundo
Fundo (Gemini):
```
uma sala técnica de estúdio profissional com um vidro grande ao fundo mostrando a sala de gravação iluminada (microfone de estúdio num pedestal, painéis acústicos), mesa de mixagem desfocada em primeiro plano atrás dele, luz fria e azulada.
```
Para o Veo: `Sala técnica de estúdio profissional à noite (vidro grande ao fundo mostrando a sala de gravação iluminada com microfone num pedestal, mesa de mixagem desfocada, luz fria azulada)`

---

## Dicas
- Confira no quadro inicial: rosto igual, mesma pose e mesmo tamanho na imagem, moletom com capuz abaixado e
  cordões pretos. Se algo mudou além do fundo, gere de novo.
- A headline e as legendas continuam iguais (brancas com contorno preto); só a capa muda de cor/fundo.
