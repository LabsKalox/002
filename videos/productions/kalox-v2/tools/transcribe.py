import sys, subprocess, json, numpy as np, sherpa_onnx
M = sys.argv[1]; media = sys.argv[2]
pcm = subprocess.run(["ffmpeg","-v","error","-i",media,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32)/32768
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f"{M}/sherpa-onnx-whisper-small/small-encoder.int8.onnx", decoder=f"{M}/sherpa-onnx-whisper-small/small-decoder.int8.onnx", tokens=f"{M}/sherpa-onnx-whisper-small/small-tokens.txt", language="pt", task="transcribe", num_threads=4)
cfg = sherpa_onnx.VadModelConfig(); cfg.silero_vad.model=f"{M}/silero_vad.onnx"; cfg.silero_vad.min_silence_duration=0.15; cfg.silero_vad.min_speech_duration=0.15; cfg.sample_rate=16000
vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=60)
ws = cfg.silero_vad.window_size; out=[]
for i in range(0, len(audio), ws):
    vad.accept_waveform(audio[i:i+ws])
    while not vad.empty():
        seg = vad.front; st = rec.create_stream(); st.accept_waveform(16000, seg.samples); rec.decode_stream(st)
        out.append({"start": round(seg.start/16000,2), "end": round((seg.start+len(seg.samples))/16000,2), "text": st.result.text.strip()}); vad.pop()
vad.flush()
while not vad.empty():
    seg = vad.front; st = rec.create_stream(); st.accept_waveform(16000, seg.samples); rec.decode_stream(st)
    out.append({"start": round(seg.start/16000,2), "end": round((seg.start+len(seg.samples))/16000,2), "text": st.result.text.strip()}); vad.pop()
print(json.dumps(out, ensure_ascii=False, indent=1))
