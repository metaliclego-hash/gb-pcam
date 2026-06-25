#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate PWA icons for GBCam using PIL (already installed)."""
from PIL import Image, ImageDraw

def make_icon(size):
    img = Image.new('RGB', (size, size), '#0f380f')
    d   = ImageDraw.Draw(img)
    s   = size

    # Camera body
    pad = s // 10
    d.rounded_rectangle(
        [pad, s * 28 // 100, s - pad, s * 72 // 100],
        radius=s // 10, fill='#306230',
    )
    # Lens outer ring
    cx, cy = s // 2, s // 2
    r = s // 4
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill='#9bbc0f')
    # Lens middle
    r2 = s // 6
    d.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], fill='#0f380f')
    # Lens inner
    r3 = s // 12
    d.ellipse([cx - r3, cy - r3, cx + r3, cy + r3], fill='#306230')
    # Viewfinder bump (top of camera body)
    bw, bh = s // 5, s // 14
    d.rectangle(
        [cx - bw // 2, s * 28 // 100 - bh, cx + bw // 2, s * 28 // 100],
        fill='#306230',
    )

    return img

make_icon(192).save('icon-192.png')
make_icon(180).save('icon-180.png')
print('Created: icon-192.png  icon-180.png')
