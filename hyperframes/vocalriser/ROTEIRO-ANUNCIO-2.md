# Vocal Riser — anúncio 2: "Para de desenhar automação de riser" (dor primeiro)

Roteiro do Lucas (16/11). Fala do começo ao fim; nas cenas do DAW a fala continua por cima (voz em off).

| Tempo | Fala | Tela |
|---|---|---|
| 0–2 s | "Para de desenhar automação de riser." | Ele falando desde o 1º quadro (sem intro, sem flash branco). PARA DE DESENHAR AUTOMAÇÃO. Riser subindo por baixo. |
| 2–5 s | "Joga o vocal no Vocal Riser e..." | DAW com o vocal, abrindo o plugin. Selo VOCAL RISER. |
| 5–9 s | "...ele faz o reverse de 1 a 4 compassos, com chorus, tremolo e phone. Dá pra ajustar tudo depois." | Um clique. REVERSE 1 A 4 COMPASSOS / CHORUS · TREMOLO · PHONE. |
| 9–11 s | "Um botão só. Riser pronto pro drop." | O riser entrando no drop (som da gravação). UM BOTÃO SÓ. |
| 11–13 s | "R$ 9,99, pagamento único." | R$ 9,99 grande + PAGAMENTO ÚNICO. |
| 13–15 s | "Roda no Mac e no Windows." | Ícones Mac e Windows. |
| 15–18 s | "Compra pelo celular, o link chega no e-mail, e você baixa no PC." | CELULAR → E-MAIL → PC. |
| 18–20 s | "Toca em Saiba mais." | Botão SAIBA MAIS + dedo apontando. |

## Plano de produção
- Takes que já existem e servem: `anuncio/assets/raw/2.mp4` ("E custa nove e noventa e nove, pagamento único. Roda no
  Mac e no Windows.") e `anuncio/assets/raw/3.mp4` ("Compra pelo celular, o link chega no e-mail e você baixa no PC. Toca
  em Saiba mais.").
- Takes novos (3): A, B e C abaixo. Mesma imagem inicial do Gemini dos takes do anúncio 1.
- A voz inteira (A+B+C+2+3) vai num único WAV para o Voice Changer, numa passada só (sem misturar versões).
- Gravação de tela com som (obrigatória): DAW com o vocal → abre o Vocal Riser → um clique → o riser entra no drop.
- Tempo real: ~68 palavras. A 1,2× (só a fala) dá ~22 s; 20 s cravados só cortando "Dá pra ajustar tudo depois" da
  fala (fica só no texto).

## Prompts do Veo (Quality, 1080p, Frames to Video, 9:16, com áudio)

**Cenário trocado de novo** (pedido do Lucas): agora é uma sala de uma casa de alto padrão, no estilo da foto de referência que ele mandou (painéis ripados de madeira escura, fita de LED branco-quente embutida no teto/estante, móveis pretos, clima sofisticado — sem estúdio de música, sem carro). Roupa também mudou: saiu o moletom com capuz, entrou uma blusa de manga longa preta larga, sem capuz e sem cordão — vale só para este vídeo; o padrão do CLAUDE.md (moletom capuz abaixado) continua para os outros. Isso precisa de uma nova imagem inicial do Gemini com esse cenário e essa roupa. Gerar o Passo 0 de novo (mesmas fotos reais dele) com o prompt abaixo antes dos 3 takes.

### Passo 0 — Gemini (quadro inicial novo, sala de casa top)
Envie 2 ou 3 fotos reais dele, nítidas, uma de frente.
```
Use estas fotos como referência de identidade. O resultado tem que ser reconhecível como esta mesma pessoa, sem dúvida: mantenha exatamente o formato do rosto e do queixo, os olhos (formato, cor, tamanho e distância entre eles, com a mesma abertura natural e relaxada das fotos, sem arregalar), as sobrancelhas, o nariz, a boca, as orelhas, o cabelo, a barba e o tom de pele. Não embeleze e não troque por outro rosto parecido. Ele tem 27 anos: só deixe a pele lisa, saudável e uniforme, sem rugas, sem manchas e sem verrugas.
Ele veste uma blusa de manga longa preta, larga, gola redonda lisa, sem capuz e sem cordão, sentado numa sala de estar de uma casa de alto padrão, à noite, olhando direto para a câmera, enquadramento de selfie vertical do peito para cima, como se ele mesmo segurasse o celular com o braço esticado. Ambiente: parede com painéis ripados de madeira escura, fita de LED branco-quente embutida correndo pelo teto e por uma estante preta ao fundo, móveis pretos foscos, decoração sofisticada e aconchegante, nada de estúdio de música ou equipamento de áudio visível. Luz suave no rosto, sem sombras duras. Fotografia nítida, alta qualidade, formato vertical, sem texto, sem logos.
```
Use essa mesma imagem nos 3 takes abaixo.

### Take A
```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de manga longa preta, larga, gola redonda lisa, sem capuz e sem cordão, igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Sala de estar de uma casa de alto padrão, à noite, igual à da imagem inicial: painéis ripados de madeira escura, fita de LED branco-quente no teto e numa estante preta ao fundo, móveis pretos foscos, nada de estúdio de música visível.
Ele já começa falando no primeiro segundo, direto para a câmera, em português do Brasil, com sotaque brasileiro, voz firme e animada, como quem dá um conselho de produtor para produtor, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Para de desenhar automação de riser. Joga o vocal no Vocal Riser."
Gestos: faz um gesto de "para" com a mão aberta na altura do peito; depois aponta para o lado, como quem mostra a tela.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

### Take B
```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de manga longa preta, larga, gola redonda lisa, sem capuz e sem cordão, igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Sala de estar de uma casa de alto padrão, à noite, igual à da imagem inicial: painéis ripados de madeira escura, fita de LED branco-quente no teto e numa estante preta ao fundo, móveis pretos foscos, nada de estúdio de música visível.
Ele olha para a câmera e fala em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Ele faz o reverse de um a quatro compassos, com chorus, tremolo e phone."
Gestos: conta nos dedos de um a quatro; depois conta três efeitos nos dedos.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

### Take C
```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de manga longa preta, larga, gola redonda lisa, sem capuz e sem cordão, igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Sala de estar de uma casa de alto padrão, à noite, igual à da imagem inicial: painéis ripados de madeira escura, fita de LED branco-quente no teto e numa estante preta ao fundo, móveis pretos foscos, nada de estúdio de música visível.
Ele olha para a câmera e fala em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Dá pra ajustar tudo depois. Um botão só, riser pronto pro drop."
Gestos: aperta um botão no ar com o dedo indicador; no fim desce a mão com força, como um drop entrando, e sorri.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

## Gravação de tela (com o som)
- 1080p, com o áudio do computador gravado junto (ou exporte o WAV do mesmo trecho).
- Sequência: o clipe de vocal na DAW → abre o Vocal Riser → um clique → o riser toca e entra no drop (deixe 2 s de drop).
- Mostre o REVERSE em 1 BAR e, se der, troque para 4 BARS; ligue CHORUS, TREMOLO e PHONE.
- 10–15 s no total; corte e exporte em 1080p para passar aqui na conversa (abaixo de ~25 MB).

## Legenda
A mesma do anúncio 1 (termina com "Comenta RISER que eu te mando o link").
