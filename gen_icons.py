#!/usr/bin/env python3
"""Generate Footsteps PWA app icons with no third-party deps (pure stdlib).

Draws gold footprints on the site's dark "ink" radial background and writes
square PNGs at the sizes a PWA needs (apple-touch 180, 192, 512). The 512 is
listed in the manifest as both "any" and "maskable" — footprints sit well
inside the central safe zone, and the background is full-bleed.
"""
import math, zlib, struct, os

INK_CENTER = (0x3a, 0x24, 0x12)   # slightly lifted ink toward the middle
INK_EDGE   = (0x20, 0x12, 0x08)   # darker ink at the corners
GOLD       = (0xf0, 0xc0, 0x40)

def clamp(v, a, b): return a if v < a else b if v > b else v
def lerp(a, b, t): return a + (b - a) * t

def foot_shapes(S):
    """Ellipses (cx, cy, rx, ry) in foot-local pixels: forefoot, heel, 4 toes."""
    sh = [(0.0, -0.030 * S, 0.072 * S, 0.090 * S),   # forefoot / ball
          (0.0,  0.090 * S, 0.050 * S, 0.072 * S)]   # heel
    for tx, ty in [(-0.050, -0.150), (-0.017, -0.162), (0.017, -0.162), (0.050, -0.150)]:
        sh.append((tx * S, ty * S, 0.020 * S, 0.022 * S))  # toes
    return sh

def render(S):
    cx, cy = S * 0.5, S * 0.5
    rad = 0.72 * S
    feet = []
    for fxN, fyN, deg in [(0.42, 0.585, -10), (0.595, 0.415, 10)]:
        a = math.radians(deg)
        feet.append((fxN * S, fyN * S, math.cos(a), math.sin(a)))
    SH = foot_shapes(S)
    px = bytearray(S * S * 4)
    for y in range(S):
        for x in range(S):
            t = clamp(math.hypot(x - cx, y - cy) / rad, 0.0, 1.0)
            r = int(lerp(INK_CENTER[0], INK_EDGE[0], t))
            g = int(lerp(INK_CENTER[1], INK_EDGE[1], t))
            b = int(lerp(INK_CENTER[2], INK_EDGE[2], t))
            cov = 0.0
            for fx, fy, ca, sa in feet:
                dx, dy = x - fx, y - fy
                lx = dx * ca + dy * sa     # rotate point into foot-local frame
                ly = -dx * sa + dy * ca
                for clx, cly, rxl, ryl in SH:
                    fdx, fdy = (lx - clx) / rxl, (ly - cly) / ryl
                    f = math.sqrt(fdx * fdx + fdy * fdy)
                    feather = 1.4 / min(rxl, ryl)
                    c = clamp((1.0 - f) / feather + 0.5, 0.0, 1.0)
                    if c > cov: cov = c
                    if cov >= 1.0: break
                if cov >= 1.0: break
            if cov > 0:
                r = int(lerp(r, GOLD[0], cov))
                g = int(lerp(g, GOLD[1], cov))
                b = int(lerp(b, GOLD[2], cov))
            i = (y * S + x) * 4
            px[i], px[i+1], px[i+2], px[i+3] = r, g, b, 255
    return px

def write_png(path, S, px):
    raw = bytearray()
    row = S * 4
    for y in range(S):
        raw.append(0)                       # filter byte 0 (None) per scanline
        raw += px[y * row:(y + 1) * row]
    comp = zlib.compress(bytes(raw), 9)
    def chunk(typ, data):
        return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
    with open(path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n'
                + chunk(b'IHDR', struct.pack('>IIBBBBB', S, S, 8, 6, 0, 0, 0))
                + chunk(b'IDAT', comp)
                + chunk(b'IEND', b''))

if __name__ == '__main__':
    os.makedirs('icons', exist_ok=True)
    for S, name in [(512, 'icon-512.png'), (192, 'icon-192.png'), (180, 'icon-180.png')]:
        write_png(os.path.join('icons', name), S, render(S))
        print('wrote icons/%s (%dx%d)' % (name, S, S))
