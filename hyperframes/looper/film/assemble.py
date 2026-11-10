"""Final assembly: only the presenter's talking section is sped up; plugin intro, plugin audio and end card stay at 1x.

Video: intro + end card from the 30 fps master, talking section from the master rendered at 30/SPEED fps
(each master frame becomes exactly one 30 fps output frame, nothing dropped).
Audio: rebuilt from the sources. Voice and SFX of the talking section follow the sped-up timing (voice with
atempo, pitch kept); the plugin's build/drop audio plays at its original speed.

usage: python3 assemble.py SPEED master30.mp4 masterFast.mp4 out.mp4
"""
import subprocess, sys
from fractions import Fraction

SPEED = float(sys.argv[1]); M30, MF, OUT = sys.argv[2:5]
FPS_F = Fraction(30) / Fraction(str(SPEED))          # e.g. 300/11 for 1.1x
T_TALK, T_END, T_TOTAL = 2.8, 20.2, 22.6             # film times (must match index.html)

f0 = -(-Fraction(str(T_TALK)) * FPS_F // 1)           # first fast-master frame at/after T_TALK
f1 = Fraction(str(T_END)) * FPS_F // 1 - 1            # last fast-master frame before T_END
talk_start_film = float(f0 / FPS_F)
n_talk = int(f1 - f0 + 1)
out_talk0 = T_TALK
out_end0 = T_TALK + n_talk / 30.0

def out_t(film_t):
    """Map a film time to the output timeline."""
    if film_t < T_TALK: return film_t
    if film_t < T_END: return out_talk0 + (film_t - talk_start_film) / SPEED
    return out_end0 + (film_t - T_END)

A = "assets/"
# (file, film_start, media_start, duration_film, volume, fade_out, sped)
clips = [
    (A + "voice/looper-voz-voicechanger-v2.wav", 2.8, 0.03, 17.4, 1.0, 0.2, True),
    (A + "sfx/whoosh.wav", 7.5, 0, 0.6, 0.22, 0, False),
    (A + "sfx/hit.wav", 7.96, 0, 0.7, 0.22, 0, False),
    (A + "sfx/pop.wav", 10.15, 0, 0.2, 0.22, 0, False),
    (A + "sfx/click.wav", 11.06, 0, 0.07, 0.22, 0, False),
    (A + "sfx/tick.wav", 11.95, 0, 0.03, 0.16, 0, False),
    (A + "sfx/tick.wav", 12.1, 0, 0.03, 0.16, 0, False),
    (A + "sfx/tick.wav", 12.25, 0, 0.03, 0.16, 0, False),
    (A + "sfx/whoosh.wav", 15.35, 0, 0.6, 0.22, 0, False),
    (A + "sfx/ding.wav", 18.87, 0, 1.3, 0.2, 0, False),
    (A + "sfx/whoosh.wav", 19.95, 0, 0.6, 0.22, 0, False),
]

inputs = ["-i", M30, "-i", MF]
fc = [
    f"[0:v]trim=start_frame=0:end_frame={int(T_TALK*30)},setpts=PTS-STARTPTS[v0]",
    f"[1:v]trim=start_frame={int(f0)}:end_frame={int(f1)+1},setpts=(PTS-STARTPTS)/{SPEED},fps=30[v1]",
    f"[0:v]trim=start_frame={int(T_END*30)}:end_frame={int(T_TOTAL*30)},setpts=PTS-STARTPTS[v2]",
    "[v0][v1][v2]concat=n=3:v=1:a=0,format=yuv420p[v]",
]
labels = []
for i, (f, fs, ms, dur, vol, fade, sped) in enumerate(clips):
    inputs += ["-i", f]
    k = i + 2
    chain = f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=start={ms}:duration={dur},asetpts=PTS-STARTPTS"
    if fade: chain += f",afade=t=out:st={dur-fade}:d={fade}"
    if sped: chain += f",atempo={SPEED}"
    start = out_t(fs) if not sped else out_talk0 + (fs - talk_start_film) / SPEED
    if start < 0: chain += f",atrim=start={-start},asetpts=PTS-STARTPTS"; start = 0
    chain += f",volume={vol},adelay={int(round(start*1000))}|{int(round(start*1000))}[a{i}]"
    fc.append(chain); labels.append(f"[a{i}]")
total_out = out_end0 + (T_TOTAL - T_END)

# Music bed = the plugin's own track at 1x, start-to-finish: build (drop kick at 19.415 s lands on the cut at
# out 2.8), full for a moment, ducked under the voice, up again on the end card. After the file ends it loops the
# post-drop section on bar lines (128 BPM, 6 bars = 11.25 s).
DROP, BAR = 19.415, 60 / 128 * 4
m0 = DROP - T_TALK
loop_end = DROP + 6 * BAR
duck0, duck1, up0 = T_TALK + 0.15, T_TALK + 0.3, out_end0 - 0.15
vol = (f"if(lt(t,{duck0}),0.8,if(lt(t,{duck1}),0.8-(t-{duck0})/({duck1}-{duck0})*0.7,"
       f"if(lt(t,{up0}),0.1,if(lt(t,{out_end0}),0.1+(t-{up0})/0.15*0.4,0.5))))")
MUS = OUT + ".music.wav"   # rendered on its own first: inside the big graph the looped part got dropped
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", A + "audio/vst-build.mp3", "-i", A + "audio/vst-build.mp3",
                "-filter_complex",
                f"[0:a]aresample=48000,aformat=channel_layouts=stereo,atrim=start={m0}:end={loop_end},asetpts=PTS-STARTPTS[m1];"
                f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=start={DROP}:end={loop_end},asetpts=PTS-STARTPTS[m2];"
                f"[m1][m2]concat=n=2:v=0:a=1,atrim=end={total_out:.3f},volume='{vol}':eval=frame,"
                f"afade=t=out:st={total_out-0.8:.3f}:d=0.8[o]", "-map", "[o]", "-c:a", "pcm_s16le", MUS], check=True)
mi = len(inputs) // 2
inputs += ["-i", MUS]
fc.append(f"[{mi}:a]asetpts=PTS-STARTPTS[mus]")
labels.insert(0, "[mus]")  # first: amix takes its start time from the first input
fc.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=end={total_out:.3f},"
          "aresample=48000[a]")
# pass 1: video + raw mix; pass 2: one static gain to -15 LUFS + true-peak limiter (keeps the build/drop dynamics;
# loudnorm's dynamic mode flattened the drop)
TMP = OUT + ".tmp.mkv"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-crf", "17", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", TMP], check=True)
m = subprocess.run(["ffmpeg", "-hide_banner", "-i", TMP, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
I = float([l for l in m.splitlines() if l.strip().startswith("I:")][-1].split()[1])
gain = -15.0 - I
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", TMP, "-c:v", "copy", "-af",
                f"volume={gain:.2f}dB,alimiter=limit=0.8:attack=1:release=50:level=false,aresample=48000",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", OUT], check=True)
import os; os.remove(TMP); os.remove(MUS)
print(f"mix {I:.1f} LUFS → gain {gain:+.1f} dB")
print(f"talk: master frames {int(f0)}–{int(f1)} (film {talk_start_film:.4f}–{float((f1+1)/FPS_F):.4f}s) → out "
      f"{out_talk0:.3f}–{out_end0:.3f}s; end card out {out_end0:.3f}–{total_out:.3f}s")
print(f"voice placed at out {out_talk0 + (2.8 - talk_start_film)/SPEED:.4f}s")
