# KaloxSooth — lançamento (análise da referência)

Fonte: `source.mp4` (envio do usuário, `KaloxSooth_lancamento_FINAL.mp4`), 26,47 s, 1080×1920,
30 fps, com áudio. A fala foi lida pelas legendas gravadas no vídeo, porque a transcrição local
(WhisperX) está bloqueada na rede deste ambiente. Os tempos têm precisão de ~0,33 s; ver `TIMELINE.md`.

## O que o vídeo faz

Um criador apresenta o próprio plugin gratuito para quem mixa música. Em 26 s o vídeo
1. promete o resultado e o preço antes de qualquer fala (headline fixa);
2. cria uma relação pessoal ("vem cá que eu vou te mostrar o que o **meu** plugin novo faz");
3. prova na tela, com o som da mix antes e depois;
4. responde às três objeções de quem compra plugin, nesta ordem: controle, mecanismo e preço;
5. fecha com CTA e uma gíria que dá personalidade.

Estrutura (minha interpretação): **Promessa → Gancho pessoal → Ponte → Prova → Objeções → CTA**.

## Sistemas visuais

### 1. Headline fixa (0–26,4 s, sem entrada nem saída)
- Duas linhas centralizadas no topo (~3–5 % da altura): "Tira o agudo ardido da mix" em
  itálico extra-negrito branco com contorno preto; "DE GRAÇA" em caixa alta, maior, mesmo estilo.
- Fica igual sobre a câmera e sobre a tela. Para o espectador: em qualquer quadro dá para entender
  a oferta, inclusive para quem entra no meio do vídeo ou assiste no loop.
- Linha 1 = dor específica do nicho ("agudo ardido"). Linha 2 = preço como gancho.

### 2. Legenda de fala (frase a frase, palavras em destaque)
- 2 a 6 palavras por bloco, no máximo 2 linhas, sans extra-negrita (estilo Montserrat Black),
  branca com algumas palavras em amarelo (#FFD400 aprox.), sombra/contorno escuro.
- Posição fixa a ~70–72 % da altura nas duas cenas, abaixo do rosto e abaixo da janela do plugin.
- Entrada em pop: o bloco aparece menor e cresce em ~0,3 s (ver 1,0 s e 2,33 s). O amarelo muda
  palavra a palavra conforme a fala; parece o estilo "destaque" automático de editor (CapCut).
- Some durante as pausas de prova sonora (7,0–8,7 s e 13,0–14,4 s).
- A legenda "olha isso aqui!" atravessa o corte para a tela (6,6 → 7,0 s) e amarra a ponte.

### 3. A-roll (0–6,8 s)
- Plano médio, estúdio com teclados e luz roxa. Moletom preto, olhar direto para a câmera.
- Gestos guiam a atenção: chamado com o polegar (0,3–1,0 s) e dedo apontando para baixo
  em "olha isso aqui" (5,3–6,8 s), justamente onde a demonstração vai aparecer.

### 4. Demonstração (6,8–26,4 s)
- Tela do computador filmada com o celular, na mão: tremida, em ângulo, com zoom. Passa autenticidade
  ("é real, é o meu computador"), mas é difícil de ler.
- Alterna dois planos: painel de controles (knobs depth/detail) e espectro (curva com nós
  verde/vermelho cortando picos). Os cortes coincidem com troca de frase (9,5 s; 13,1 s; ~18 s; ~22,5 s).
- Ação do cursor no knob em "dá pra ajustar tudo depois" (controle demonstrado, não só dito).

### 5. Áudio
- Voz do criador o tempo todo, com duas janelas sem fala em que a mix toca (prova sonora).
  Ainda não confirmei de ouvido se há antes/depois; é a hipótese mais provável.

## Por que prende (interpretação)
1. **Oferta legível em 1 s**: dor do nicho + "DE GRAÇA" no topo, sem depender do áudio.
2. **Fala pessoal e informal**: "meu plugin novo", "doideira", "o bagulho é louco". Soa como criador, não como marca.
3. **Ponte gestual**: o dedo aponta para baixo e a tela entra. A atenção é entregue, não cortada.
4. **Prova antes de argumento**: a tela entra aos 6,8 s e não sai mais.
5. **Sequência de objeções em perguntas e respostas curtas**: "E o custo? / Nada. / É de graça, / tá de graça."
   A repetição martela o preço logo antes do CTA.

## Pontos fracos e oportunidades
- **A prova principal é sonora, e muita gente assiste sem som.** Nas janelas de prova (7–8,7 s,
  13–14,4 s) não há legenda nem indicação visual. Oportunidade: rótulo "ANTES / DEPOIS" ou
  "🔊 liga o som" e destaque visual do corte no espectro.
- **Tela filmada com o celular, ilegível em vários trechos.** Gravação de tela com zoom em
  movimento manteria a autenticidade e ganharia clareza. Trade-off: perde o "feito à mão".
- **Primeiro segundo sem fala nem legenda** (só o gesto). Funciona porque a headline segura,
  mas é o trecho mais arriscado para a retenção.
- **CTA sem apoio visual**: "link na bio" não aparece na tela de forma diferente das outras legendas.

## O que vira template (estrutura reaproveitável)
| Bloco | Tempo ref. | Função | Variável no template |
|---|---|---|---|
| Headline fixa | 0–fim | Dor + oferta | `headline.linha1`, `headline.linha2` |
| Gancho A-roll | 0–6,8 s | Chamado + promessa pessoal + gesto de ponte | clipe de câmera, frases |
| Prova 1 + controle | 6,8–13 s | Mostrar funcionando | clipe de tela/produto |
| Pausa de prova | 13–14,4 s | Deixar o resultado falar | rótulo opcional |
| Mecanismo | 14,5–18 s | Como funciona, em 1 frase | frase |
| Preço Q&A | 18–22,3 s | Pergunta → resposta seca → repetição | frases |
| CTA + assinatura | 22,4–26,4 s | Link + gíria de fechamento | frases |
