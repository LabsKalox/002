# Vocal Riser — anúncio 3 (versão Meta): roteiro + prompts do Veo

**Objetivo:** deixar óbvio que é um **plugin de áudio** (a Meta recusou a versão anterior achando que era venda de engajamento/contas).
**Formato final:** 1080×1920, 30 fps, 15–18 s, MP4 H.264 + AAC. Texto só dentro de y=270–1250 (eu faço na edição).
**Veo:** Quality, 1080p, Frames to Video, 9:16, com áudio. MESMA imagem inicial (Passo 0 do Gemini) nos 5 takes. Cada take fala UMA vez, sem pausa no começo.
**Voz:** fala original do Veo → guia (eu monto) → Voice Changer do ElevenLabs com o clone → volta sem edição.

## Roteiro (o que ele fala, take a take)

| Take | Fala (exata) | Tela (eu monto) | Status |
|---|---|---|---|
| **T1-B** | "Esse plugin cria um riser de vocal com um clique." | Texto fixo PLUGIN DE ÁUDIO · VST3 · AU, plugin aparece, riser tocando | **NOVO — gerar** |
| T2 | "Ele faz o reverse de um a quatro compassos, com chorus, tremolo e phone." | Plugin: REVERSE 1→4, liga CHORUS, TREMOLO, PHONE | já tem (voz pronta) |
| T3 | "E dá pra ajustar depois. Sem desenhar automação nenhuma." | AJUSTA TUDO DEPOIS; riser entra no drop | já tem (voz pronta) |
| T4 | "Nove e noventa e nove, pagamento único. Mac e Windows." | VOCAL RISER BY KALOX · R$ 9,99 · pagamento único · Mac e Windows | já tem (voz pronta) |
| T5 | "Compra pelo celular, o link vai pro seu e-mail, e você baixa no PC. Toca em Saiba mais." | Celular → e-mail → PC → SAIBA MAIS | já tem (voz pronta) |

**Só o T1 muda.** Se você quiser refazer o vídeo inteiro do zero, gere os 5 com os prompts abaixo; se não, gere só o T1-B e eu reaproveito T2–T5.

**Palavras proibidas em fala e texto:** garantido, o melhor, ganhe, viralize, seguidores, curtidas, views, engajamento, "comenta". Nada de comparar com outros produtos.

**Se o Veo errar uma palavra** (principalmente "plugin" ou "riser"), gere de novo: troca de palavra no áudio eu não conserto.

## Passo 0 — Gemini (imagem inicial, igual às anteriores)
Use o Passo 0 de `VEO-PROMPTS-ANUNCIO-3.md` (fotos reais dele + foto do estúdio de referência), sem LED, blusa preta manga longa.

## T1-B — NOVA abertura (versão aprovável pela Meta: diz que é um plugin)

Troca o T1. Mesma imagem inicial, mesmas regras. Depois: Voice Changer com o clone dele (guia 1x → volta sem edição), como nos outros takes.

```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de MANGA LONGA toda preta, larga, de algodão fosco, gola redonda lisa, sem capuz, sem cordão, sem estampa e sem logo. As mangas são compridas e cobrem os braços inteiros até os punhos o tempo todo, inclusive quando ele levanta o braço ou a mão; nunca manga curta, nunca camiseta, nunca braço ou antebraço de fora, nunca mangas arregaçadas. Igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Estúdio de música escuro à noite, igual ao da imagem de referência, mas com todas as luzes de LED removidas: parede de painéis acústicos pretos ripados, teto e paredes lisos e escuros sem nenhuma linha luminosa, dois monitores curvos atrás dele mostrando um software de música com ondas sonoras (desfocados), uma caixa de som de estúdio à direita, fones de ouvido na mesa, cadeira gamer preta com detalhes verdes. A única iluminação é uma luz baixa, quente e difusa de ambiente, deixando o fundo na penumbra. Sem fitas de LED, sem ring light, sem neon, sem luzes coloridas, sem nenhum outro objeto de iluminação.
Ele já começa falando no primeiro segundo, sem pausa, direto para a câmera, em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Esse plugin cria um riser de vocal com um clique."
Gestos: apresenta com a mão aberta, como quem mostra algo na frente dele, sorrindo; no fim aperta um botão no ar com o dedo indicador.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

## T2 — Reverse / efeitos

```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de MANGA LONGA toda preta, larga, de algodão fosco, gola redonda lisa, sem capuz, sem cordão, sem estampa e sem logo. As mangas são compridas e cobrem os braços inteiros até os punhos o tempo todo, inclusive quando ele levanta o braço ou a mão; nunca manga curta, nunca camiseta, nunca braço ou antebraço de fora, nunca mangas arregaçadas. Igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Estúdio de música escuro à noite, igual ao da imagem de referência, mas com todas as luzes de LED removidas: parede de painéis acústicos pretos ripados, teto e paredes lisos e escuros sem nenhuma linha luminosa, dois monitores curvos atrás dele mostrando um software de música com ondas sonoras (desfocados), uma caixa de som de estúdio à direita, fones de ouvido na mesa, cadeira gamer preta com detalhes verdes. A única iluminação é uma luz baixa, quente e difusa de ambiente, deixando o fundo na penumbra. Sem fitas de LED, sem ring light, sem neon, sem luzes coloridas, sem nenhum outro objeto de iluminação.
Ele já começa falando no primeiro segundo, sem pausa, direto para a câmera, em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Ele faz o reverse de um a quatro compassos, com chorus, tremolo e phone."
Gestos: conta nos dedos de um a quatro; depois conta três efeitos nos dedos.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

## T3 — "Sem automação"

```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de MANGA LONGA toda preta, larga, de algodão fosco, gola redonda lisa, sem capuz, sem cordão, sem estampa e sem logo. As mangas são compridas e cobrem os braços inteiros até os punhos o tempo todo, inclusive quando ele levanta o braço ou a mão; nunca manga curta, nunca camiseta, nunca braço ou antebraço de fora, nunca mangas arregaçadas. Igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Estúdio de música escuro à noite, igual ao da imagem de referência, mas com todas as luzes de LED removidas: parede de painéis acústicos pretos ripados, teto e paredes lisos e escuros sem nenhuma linha luminosa, dois monitores curvos atrás dele mostrando um software de música com ondas sonoras (desfocados), uma caixa de som de estúdio à direita, fones de ouvido na mesa, cadeira gamer preta com detalhes verdes. A única iluminação é uma luz baixa, quente e difusa de ambiente, deixando o fundo na penumbra. Sem fitas de LED, sem ring light, sem neon, sem luzes coloridas, sem nenhum outro objeto de iluminação.
Ele já começa falando no primeiro segundo, sem pausa, direto para a câmera, em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"E dá pra ajustar depois. Sem desenhar automação nenhuma."
Gestos: gira a mão no ar como quem ajusta um botão; depois balança o dedo indicador dizendo "não", sorrindo.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

## T4 — Preço

```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de MANGA LONGA toda preta, larga, de algodão fosco, gola redonda lisa, sem capuz, sem cordão, sem estampa e sem logo. As mangas são compridas e cobrem os braços inteiros até os punhos o tempo todo, inclusive quando ele levanta o braço ou a mão; nunca manga curta, nunca camiseta, nunca braço ou antebraço de fora, nunca mangas arregaçadas. Igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto. Estúdio de música escuro à noite, igual ao da imagem de referência, mas com todas as luzes de LED removidas: parede de painéis acústicos pretos ripados, teto e paredes lisos e escuros sem nenhuma linha luminosa, dois monitores curvos atrás dele mostrando um software de música com ondas sonoras (desfocados), uma caixa de som de estúdio à direita, fones de ouvido na mesa, cadeira gamer preta com detalhes verdes. A única iluminação é uma luz baixa, quente e difusa de ambiente, deixando o fundo na penumbra. Sem fitas de LED, sem ring light, sem neon, sem luzes coloridas, sem nenhum outro objeto de iluminação.
Ele já começa falando no primeiro segundo, sem pausa, direto para a câmera, em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Nove e noventa e nove, pagamento único. Mac e Windows."
Gestos: junta o polegar e o indicador mostrando "pouquinho"; depois aponta para um lado e para o outro com a mão aberta.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

## T5 — Compra pelo celular

```
Selfie vertical 9:16, câmera frontal do celular com o braço esticado, estável. O mesmo homem da imagem inicial, com o rosto idêntico ao da imagem em todos os quadros (mesmos olhos, relaxados e nunca arregalados, nariz, boca, cabelo e barba; pele lisa, sem rugas e sem manchas). Blusa de MANGA LONGA toda preta, larga, de algodão fosco, gola redonda lisa, sem capuz, sem cordão, sem estampa e sem logo. As mangas são compridas e cobrem os braços inteiros até os punhos o tempo todo, inclusive quando ele levanta o braço ou a mão; nunca manga curta, nunca camiseta, nunca braço ou antebraço de fora, nunca mangas arregaçadas. Igual em todos os quadros, sem trocar de roupa. Mãos vazias, nunca na frente do rosto, nenhum celular, telefone ou objeto na mão. Estúdio de música escuro à noite, igual ao da imagem de referência, mas com todas as luzes de LED removidas: parede de painéis acústicos pretos ripados, teto e paredes lisos e escuros sem nenhuma linha luminosa, dois monitores curvos atrás dele mostrando um software de música com ondas sonoras (desfocados), uma caixa de som de estúdio à direita, fones de ouvido na mesa, cadeira gamer preta com detalhes verdes. A única iluminação é uma luz baixa, quente e difusa de ambiente, deixando o fundo na penumbra. Sem fitas de LED, sem ring light, sem neon, sem luzes coloridas, sem nenhum outro objeto de iluminação.
Ele já começa falando no primeiro segundo, sem pausa, direto para a câmera, em português do Brasil, com sotaque brasileiro, voz animada e natural, bem articulado, exatamente esta frase, uma vez só, sem trocar nenhuma palavra:
"Compra pelo celular, o link vai pro seu e-mail, e você baixa no PC. Toca em Saiba mais."
Gestos: conta nos dedos enquanto fala os passos; no fim aponta para baixo com o dedo indicador e dá uma piscadinha.
Áudio: só a voz dele, sem música. Sem legendas e sem texto na tela.
```

Depois de gerar o T1-B: me mande o MP4 aqui. Eu devolvo o guia em WAV para o Voice Changer; você me manda o WAV de volta e eu entrego o v5 (estimativa 17,9–18,2 s; se passar de 18 s tiro o respiro final).
