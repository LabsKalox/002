# Ferramentas de conferência dos vídeos (usadas em todas as entregas)

Requisitos: ffmpeg, python3 com `numpy pillow sherpa-onnx` (`pip install numpy pillow sherpa-onnx`).

- `transcribe.py MODELS MIDIA` — transcreve (pt) com Whisper small int8 + VAD Silero (sherpa-onnx). MODELS é uma pasta com
  `sherpa-onnx-whisper-small/` (small-encoder.int8.onnx, small-decoder.int8.onnx, small-tokens.txt) e `silero_vad.onnx`,
  baixados das releases do sherpa-onnx no GitHub (k2-fsa/sherpa-onnx, tags `asr-models` e `asr-models`/silero_vad).
  Uso: conferir a fala do arquivo final antes de entregar.
- `vrsync.py GUIA.wav VOZ.wav` — atraso da voz em relação à fala original do Veo (correlação de envelope, global e por
  janela de 0,6 s). Usar no Voice Changer (cortar só o atraso inicial) e no arquivo final (alinhar as janelas ao
  início da fala: cortar o final no ponto em que a fala começa e comparar com o guia sem atraso).
- `vrfine.py GUIA.wav VOZ.wav INI FIM` — envelope lado a lado, para checar sílaba por sílaba onde o vrsync destoar.
- `piclag.py FONTE.mp4 FINAL.mp4 TRIM INICIO_CLIPE T0 T1 "lambda t: escala"` — confere qual quadro do take original
  aparece em cada quadro do render (imagem atrasada/adiantada).

Montagem final (só a fala acelera, sem pular quadros): `hyperframes/looper/film/assemble.py`.
