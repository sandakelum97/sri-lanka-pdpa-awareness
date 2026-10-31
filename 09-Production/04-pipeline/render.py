"""Render a 9:16 explainer from a timeline spec.
Scenes: {"type":"card","card":"open","dur":4,"cap":"c1"} or {"type":"clip","src":"path.mp4","in":0,"dur":5,"cap":"c3","zoom":1.35}
Clip scenes: the 16:9 Gemini footage is scaled+cropped to 9:16 and zoomed slightly so any baked-in text falls outside the frame; a dark gradient is added where the caption sits.
Output: <name>.mp4 (silent video track if no VO) + <name>.vtt with the caption timings.
"""
import json, subprocess, sys, os, shlex
spec = json.load(open(sys.argv[1])); name = spec['name']; cards = spec['cards_dir']; outdir = spec.get('out', '.')
FPS, W, H = 30, 1080, 1920
os.makedirs(f'{outdir}/scenes', exist_ok=True)
t = 0.0; files = []; vtt = ['WEBVTT', '']
def ts(x): m, s = divmod(x, 60); return f"00:{int(m):02d}:{s:06.3f}"
for i, sc in enumerate(spec['scenes']):
    out = f"{outdir}/scenes/{i:02d}.mp4"; tmp = out + '.tmp.mp4'; d = sc['dur']
    cap = sc.get('cap')
    overlay = f"[v][cap]overlay=0:0:format=auto[v2]" if cap else ""
    if sc['type'] == 'card':
        inputs = ['-framerate', str(FPS), '-i', f"{cards}/card-{sc['card']}.png"]
        vf = f"[0:v]format=yuv420p,loop=-1:1,trim=duration={d},setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.3,fade=t=out:st={d-0.3}:d=0.3[v]"
    else:
        z = sc.get('zoom', 1.3)
        inputs = ['-ss', str(sc.get('in', 0)), '-t', str(d), '-i', sc['src']]
        # scale so height fills 1920*z, crop centre to 1080x1920, slow push-in, gradient band
        vf = (f"[0:v]fps={FPS},scale=-2:{int(H*z)},crop={W}:{H}:(iw-{W})/2:(ih-{H})*{sc.get('cy',0.6)},setsar=1,"
              f"drawbox=x=0:y={H-640}:w={W}:h=640:color=0x14213D@0.35:t=fill,format=yuv420p,"
              f"fade=t=in:st=0:d=0.3,fade=t=out:st={d-0.3}:d=0.3[v]")
    if cap:
        inputs += ['-framerate', str(FPS), '-i', f"{cards}/cap-{cap}.png"]
        vf += f";[{1 if sc['type']=='card' else 1}:v]format=rgba,loop=-1:1,trim=duration={d},setpts=PTS-STARTPTS[cap];" + overlay
        mapv = '[v2]'
    else:
        mapv = '[v]'
    cmd = ['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', vf, '-map', mapv, '-r', str(FPS), '-t', str(d),
           '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-an', tmp]
    r = subprocess.run(cmd)
    if r.returncode != 0: print('scene failed', i, ' '.join(shlex.quote(c) for c in cmd)); sys.exit(1)
    os.replace(tmp, out); files.append(out)
    if cap:
        text = next(c['text'] for c in spec['captions'] if c['id'] == cap)
        vtt += [f"{ts(t)} --> {ts(t+d)}", text, '']
    t += d
open(f'{outdir}/concat.txt', 'w').write('\n'.join(f"file '{os.path.abspath(f)}'" for f in files))
final = f"{outdir}/{name}.mp4"
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{outdir}/concat.txt', '-c', 'copy', final + '.tmp.mp4'], check=True)
if spec.get('audio'):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', final + '.tmp.mp4', '-i', spec['audio'], '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', final], check=True); os.remove(final + '.tmp.mp4')
else:
    os.replace(final + '.tmp.mp4', final)
open(f'{outdir}/{name}.vtt', 'w').write('\n'.join(vtt))
print('done', final, f'{t:.1f}s')
