# Renders a retimed clip frame-exactly from a .pieces.json map: every output frame k (30 fps) shows the
# source frame nearest to its mapped source time. No per-piece filters, so no dropped or rounded frames.
# usage: tools-render-pieces.py <clip> <pieces.json> <out.mp4>
import json, subprocess, sys, numpy as np
clip, pj, out = sys.argv[1:4]
pieces = json.load(open(pj))
info = subprocess.run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height,r_frame_rate","-of","csv=p=0",clip],capture_output=True,text=True,check=True).stdout.strip().split(",")
W, H = int(info[0]), int(info[1]); num, den = map(int, info[2].split("/")); src_fps = num/den
targets = []
for t0, t1, s0, s1 in pieces:
    for k in range(int(t0), int(t1)):
        frac = (k - t0) / (t1 - t0); targets.append(s0 + frac*(s1 - s0))
want = [int(round(s*src_fps)) for s in targets]
fsize = W*H*3//2
dec = subprocess.Popen(["ffmpeg","-v","error","-i",clip,"-f","rawvideo","-pix_fmt","yuv420p","-"],stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","yuv420p","-s",f"{W}x{H}","-r","30","-i","-","-c:v","libx264","-crf","16","-preset","medium","-pix_fmt","yuv420p",out],stdin=subprocess.PIPE)
cur_idx, cur = -1, None
for w in want:
    while cur_idx < w:
        buf = dec.stdout.read(fsize)
        if len(buf) < fsize: break
        cur, cur_idx = buf, cur_idx + 1
    enc.stdin.write(cur)
enc.stdin.close(); enc.wait(); dec.stdout.close(); dec.wait()
print(out, len(want), "frames")
