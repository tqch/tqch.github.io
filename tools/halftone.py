#!/usr/bin/env python3
"""Convert a portrait photo into a newspaper-halftone print.

Usage:
    python3 tools/halftone.py <input> <output> [--cell N] [--max-dot N]
                                                [--ink HEX] [--paper HEX]
                                                [--size N] [--jitter N]
                                                [--style dot|line]

Defaults match the site's heritage palette:
  walnut ink (#1f1812) on cowhide cream (#f0e6d0), cell 8px at 800px,
  max dot radius 5px, 0.6px positional jitter for handmade feel.
"""
from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter


def hex_to_rgb(s: str) -> tuple[int, int, int]:
    s = s.lstrip("#")
    if len(s) != 6:
        raise ValueError(f"expected 6-digit hex, got {s!r}")
    return tuple(int(s[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def square_crop(img: Image.Image) -> Image.Image:
    w, h = img.size
    s = min(w, h)
    return img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))


def halftone(
    src: Path,
    dst: Path,
    cell: int = 8,
    max_dot: float = 5.0,
    ink: tuple[int, int, int] = (31, 24, 18),
    paper: tuple[int, int, int] = (240, 230, 208),
    out_size: int = 800,
    jitter: float = 0.6,
    contrast: float = 1.30,
    style: str = "dot",
) -> None:
    img = Image.open(src).convert("RGB")
    img = square_crop(img).resize((out_size, out_size), Image.LANCZOS)

    gray = img.convert("L")
    gray = ImageEnhance.Contrast(gray).enhance(contrast)
    gray = gray.filter(ImageFilter.GaussianBlur(radius=max(1.0, cell / 2.5)))

    out = Image.new("RGB", (out_size, out_size), paper)
    draw = ImageDraw.Draw(out, "RGBA")

    px = gray.load()
    rng = random.Random(42)  # deterministic jitter

    for y in range(0, out_size, cell):
        for x in range(0, out_size, cell):
            # Average brightness in cell
            total = 0
            count = 0
            for dy in range(cell):
                for dx in range(cell):
                    yy, xx = y + dy, x + dx
                    if 0 <= xx < out_size and 0 <= yy < out_size:
                        total += px[xx, yy]
                        count += 1
            avg = total / count if count else 0
            darkness = 1.0 - (avg / 255.0)
            r = darkness * max_dot

            if r < 0.35:
                continue

            cx = x + cell / 2 + (rng.random() - 0.5) * jitter * 2
            cy = y + cell / 2 + (rng.random() - 0.5) * jitter * 2

            if style == "line":
                # Horizontal line of width proportional to darkness; rough engraving feel.
                w = max(0.6, r)
                draw.line([(x, cy), (x + cell, cy)], fill=ink + (255,), width=int(round(w)))
            else:
                draw.ellipse(
                    [cx - r, cy - r, cx + r, cy + r],
                    fill=ink + (255,),
                )

    # A whisper of softening to mimic ink absorbing into paper.
    out = out.filter(ImageFilter.GaussianBlur(radius=0.45))

    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.suffix.lower() in {".jpg", ".jpeg"}:
        out.save(dst, "JPEG", quality=92, optimize=True)
    else:
        out.save(dst, optimize=True)
    print(f"wrote {dst}  ({out_size}×{out_size}, cell={cell}, dot≤{max_dot})")


HERITAGE_PALETTE: list[tuple[int, int, int]] = [
    # Bold UT × RRL poster — burnt-orange spirit, but with enough gradation
    # in the skin range that faces don't collapse into 2-3 mega-zones.
    # Sorted roughly by luminance so adjacent palette entries are visually
    # related, which helps the cluster-then-map step land sensibly.
    (24, 20, 16),     # walnut deep   — hair, glasses, blackest blacks
    (62, 48, 36),     # warm shadow   — cocoa under-tones
    (110, 64, 38),    # deep terracotta — face shadow
    (140, 59, 42),    # brick         — mid shadow (warm)
    (175, 95, 50),    # burnt sienna  — face midtone
    (191, 87, 0),     # UT burnt orange — accent / hot highlight
    (210, 145, 85),   # warm tan      — face highlight
    (184, 150, 90),   # brass         — mid-warm
    (235, 200, 150),  # peach cream   — skin brightest
    (240, 230, 208),  # cream         — paper highlight
    (62, 78, 108),    # faded indigo  — denim only
]

SKIN_PALETTE: list[tuple[int, int, int]] = [
    # 7-color screen-print palette. A "warm shadow" sits between walnut and
    # sienna so neutral darks have a warm option — without it, dim pixels
    # keep getting yanked into indigo (causing the bright-blue jacket specks).
    (24, 20, 16),      # walnut       — hair, glasses, deepest blacks
    (62, 48, 36),      # warm shadow  — face deep shadow, hair edges
    (110, 78, 58),     # sienna       — skin shadow
    (165, 120, 92),    # cinnamon     — skin midtone
    (215, 168, 130),   # tan          — skin highlight
    (240, 215, 185),   # bone         — shirt, brightest skin
    (62, 78, 108),     # indigo       — denim only
]

MONO_PALETTE: list[tuple[int, int, int]] = [
    # Engraving / single-ink wanted poster — 4 walnut shades on cream.
    (31, 24, 18),
    (84, 60, 42),
    (148, 110, 78),
    (240, 230, 208),
]

PALETTES: dict[str, list[tuple[int, int, int]]] = {
    "skin": SKIN_PALETTE,
    "heritage": HERITAGE_PALETTE,
    "mono": MONO_PALETTE,
}


def _build_palette_image(palette: list[tuple[int, int, int]]) -> Image.Image:
    """Build a P-mode image carrying a custom palette for quantize()."""
    pim = Image.new("P", (16, 16))
    flat: list[int] = []
    for r, g, b in palette:
        flat.extend([r, g, b])
    flat.extend([0] * (768 - len(flat)))
    pim.putpalette(flat)
    return pim


def _perceptual_distance(
    c1: tuple[int, int, int],
    c2: tuple[int, int, int],
    cool_threshold: int = 50,
) -> float:
    """Weighted RGB distance with a hue-compatibility penalty.

    Base: green-weighted Euclidean (green carries most luminance).
    Penalty: if the target palette entry is strongly cool (B - R > 30)
    but the source cluster centroid is *not* strongly cool
    (B - R < cool_threshold), we multiply the distance by 8. This keeps
    denim-blue (B-R ~50+) mapping to indigo while preventing mild-blue
    eye-area / lens-reflection clusters from doing so.
    """
    dr = c1[0] - c2[0]
    dg = c1[1] - c2[1]
    db = c1[2] - c2[2]
    base = 2.0 * dr * dr + 4.0 * dg * dg + 1.0 * db * db

    src_cool_bias = c1[2] - c1[0]
    tgt_cool_bias = c2[2] - c2[0]
    if tgt_cool_bias > 30 and src_cool_bias < cool_threshold:
        base *= 8.0

    return base


def _cluster_then_map(
    rgb: Image.Image,
    palette: list[tuple[int, int, int]],
    n_clusters: int = 24,
    cool_threshold: int = 50,
) -> Image.Image:
    """Posterize via two-step quantization.

    1. Free-quantize to ``n_clusters`` natural colour clusters using
       median-cut. PIL chooses centroids that fit the actual image — so
       skin shadows, denim shadows, hair, etc. each end up as one cluster.
    2. Map each cluster centroid to its nearest palette colour using a
       perceptually weighted distance, then re-encode.

    The result has clean, contiguous regions (no per-pixel speckling) and
    fewer mismapped colours, because the decision is made once per region
    instead of once per pixel.
    """
    if n_clusters > 256:
        n_clusters = 256
    natural = rgb.quantize(
        colors=n_clusters,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )

    raw = natural.getpalette() or []
    cluster_rgbs = [tuple(raw[i * 3 : i * 3 + 3]) for i in range(n_clusters)]  # type: ignore[misc]

    new_flat: list[int] = []
    for c in cluster_rgbs:
        best = min(palette, key=lambda p: _perceptual_distance(c, p, cool_threshold))
        new_flat.extend(best)
    new_flat.extend([0] * (768 - len(new_flat)))
    natural.putpalette(new_flat)
    return natural.convert("RGB")


def _alpha_from_white_bg(
    img: Image.Image,
    threshold: int,
    saturation_max: int,
    feather: float,
) -> Image.Image:
    """Return an L-mode alpha channel where near-white BG becomes 0.

    A pixel is treated as background when all three channels are above
    `threshold` AND the channel range (max-min) is below `saturation_max`
    — so colored cream/brass highlights aren't wiped out, only true white.
    """
    rgb = img.convert("RGB")
    px = rgb.load()
    w, h = rgb.size
    alpha = Image.new("L", (w, h), 255)
    apx = alpha.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            mn, mx = min(r, g, b), max(r, g, b)
            if mn > threshold and (mx - mn) < saturation_max:
                apx[x, y] = 0
    if feather > 0:
        alpha = alpha.filter(ImageFilter.GaussianBlur(radius=feather))
    return alpha


def write_clean(
    src: Path,
    dst: Path,
    size: int = 600,
    mode: str = "pixelate",
    palette_name: str = "skin",
    palette: list[tuple[int, int, int]] | None = None,
    bg_threshold: int = 235,
    bg_saturation_max: int = 18,
    bg_feather: float = 1.4,
    quality: int = 80,
    contrast: float = 1.0,
    dither: str = "none",
    presoften: float = 1.0,
    presoften_median: int = 3,
    postsoften_median: int = 1,
    n_clusters: int = 24,
    direct_quantize: bool = False,
    cool_threshold: int = 50,
    block: int = 20,
    blocky_alpha: bool = False,
) -> None:
    """Write the hover-reveal companion image.

    mode="pixelate" (default): block-average the image into chunky pixels
    on a transparent background. Simple, recognizable as anonymized.

    mode="posterize": quantize to a curated heritage palette (Risograph
    print look). Less reliable for portraits but available.

    mode="photo": fallback — a downscaled JPEG of the source.
    """
    img = Image.open(src).convert("RGBA")
    img = square_crop(img).resize((size, size), Image.LANCZOS)

    if mode == "photo":
        rgb = img.convert("RGB")
        if dst.suffix.lower() not in {".jpg", ".jpeg"}:
            dst = dst.with_suffix(".jpg")
        dst.parent.mkdir(parents=True, exist_ok=True)
        rgb.save(dst, "JPEG", quality=quality, optimize=True)
        print(f"wrote {dst}  ({size}×{size}, photo q={quality})")
        return

    if mode == "pixelate":
        # Background → alpha (smooth or blocky)
        alpha = _alpha_from_white_bg(img, bg_threshold, bg_saturation_max, bg_feather)

        small = max(2, size // max(1, block))
        rgb = img.convert("RGB")
        rgb_small = rgb.resize((small, small), Image.BOX)         # area average
        rgb_blocky = rgb_small.resize((size, size), Image.NEAREST)

        if blocky_alpha:
            a_small = alpha.resize((small, small), Image.BOX)
            alpha = a_small.resize((size, size), Image.NEAREST)

        out = rgb_blocky.convert("RGBA")
        out.putalpha(alpha)

        if dst.suffix.lower() != ".png":
            dst = dst.with_suffix(".png")
        dst.parent.mkdir(parents=True, exist_ok=True)
        out.save(dst, "PNG", optimize=True)
        print(
            f"wrote {dst}  ({size}×{size}, pixelate {small}×{small} blocks "
            f"≈ {block}px each, alpha={'blocky' if blocky_alpha else 'smooth'}, transparent BG)"
        )
        return

    # ---- posterize mode ----
    if palette is None:
        palette = PALETTES.get(palette_name, SKIN_PALETTE)

    # Background → alpha = 0
    alpha = _alpha_from_white_bg(img, bg_threshold, bg_saturation_max, bg_feather)

    rgb_input = img.convert("RGB")

    # Heavy median pre-pass: removes JPEG block-noise and fine speckles
    # without softening edges (median preserves boundaries unlike Gaussian).
    if presoften_median >= 1:
        size_med = int(presoften_median) * 2 + 1
        rgb_input = rgb_input.filter(ImageFilter.MedianFilter(size=size_med))

    # Tiny Gaussian smoothing on top — joins cluster centroids together.
    if presoften > 0:
        rgb_input = rgb_input.filter(ImageFilter.GaussianBlur(radius=presoften))

    if abs(contrast - 1.0) > 1e-3:
        rgb_input = ImageEnhance.Contrast(rgb_input).enhance(contrast)

    # Two-step quantize: cluster → map. Yields clean regions instead of
    # per-pixel speckling. Falls back to direct palette quantize if the
    # user explicitly asked for it.
    if direct_quantize:
        dither_map = {
            "none": Image.Dither.NONE,
            "floyd": Image.Dither.FLOYDSTEINBERG,
            "ordered": getattr(Image.Dither, "ORDERED", Image.Dither.NONE),
        }
        dither_mode = dither_map.get(dither, Image.Dither.NONE)
        pim = _build_palette_image(palette)
        posterized = rgb_input.quantize(palette=pim, dither=dither_mode).convert("RGB")
    else:
        posterized = _cluster_then_map(
            rgb_input, palette, n_clusters=n_clusters, cool_threshold=cool_threshold
        )

    # Post median: kills any remaining isolated palette islands so the
    # final regions are clean and printable-looking.
    if postsoften_median >= 1:
        size_med = int(postsoften_median) * 2 + 1
        posterized = posterized.filter(ImageFilter.MedianFilter(size=size_med))

    quantized_rgba = posterized.convert("RGBA")
    quantized_rgba.putalpha(alpha)

    if dst.suffix.lower() != ".png":
        dst = dst.with_suffix(".png")
    dst.parent.mkdir(parents=True, exist_ok=True)
    quantized_rgba.save(dst, "PNG", optimize=True)
    algo = "direct" if direct_quantize else f"cluster→map (n={n_clusters})"
    print(
        f"wrote {dst}  ({size}×{size}, posterize palette={palette_name} "
        f"({len(palette)} colors), {algo}, transparent BG)"
    )


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("src", type=Path, help="input photo (any format Pillow reads)")
    ap.add_argument("dst", type=Path, help="output image (.png or .jpg)")
    ap.add_argument("--cell", type=int, default=8, help="halftone cell size in pixels")
    ap.add_argument("--max-dot", type=float, default=5.0, help="max dot radius in pixels")
    ap.add_argument("--ink", default="#1f1812", help="ink colour (hex)")
    ap.add_argument("--paper", default="#f0e6d0", help="paper colour (hex)")
    ap.add_argument("--size", type=int, default=800, help="output square size")
    ap.add_argument("--jitter", type=float, default=0.6, help="dot positional jitter")
    ap.add_argument("--contrast", type=float, default=1.30, help="contrast boost on luma")
    ap.add_argument("--style", choices=("dot", "line"), default="dot", help="dot or engraved line")
    ap.add_argument("--clean", type=Path, default=None,
                    help="also write a clean reveal image (default: posterized PNG with transparent BG)")
    ap.add_argument("--clean-size", type=int, default=600, help="clean reveal size (default 600)")
    ap.add_argument("--clean-mode", choices=("pixelate", "posterize", "photo"), default="pixelate",
                    help="pixelate (default) = block-averaged mosaic + transparent BG; "
                         "posterize = palette quantize; photo = downscaled JPEG")
    ap.add_argument("--clean-block", type=int, default=20,
                    help="pixelate block size in pixels (default 20 → 30 blocks across a 600px output)")
    ap.add_argument("--clean-blocky-alpha", action="store_true",
                    help="also pixelate the alpha channel (Minecraft-style hard silhouette)")
    ap.add_argument("--clean-bg-threshold", type=int, default=235,
                    help="pixels brighter than this on all channels are candidates for transparent BG")
    ap.add_argument("--clean-bg-saturation-max", type=int, default=18,
                    help="and only become transparent if their channel range stays below this")
    ap.add_argument("--clean-bg-feather", type=float, default=1.4,
                    help="alpha-edge softening (in pixels) — higher = smoother cut-out")
    ap.add_argument("--clean-palette", choices=tuple(PALETTES.keys()), default="skin",
                    help="palette preset for posterize mode (default: skin — naturalistic)")
    ap.add_argument("--clean-dither", choices=("none", "floyd", "ordered"), default="none",
                    help="quantizer dither — only used when --clean-direct is set")
    ap.add_argument("--clean-presoften", type=float, default=1.0,
                    help="Gaussian blur radius applied before quantize")
    ap.add_argument("--clean-presoften-median", type=int, default=3,
                    help="median filter radius before quantize (kills JPEG speckles, preserves edges)")
    ap.add_argument("--clean-postsoften-median", type=int, default=1,
                    help="median filter radius after quantize (removes isolated palette specks)")
    ap.add_argument("--clean-clusters", type=int, default=24,
                    help="natural color clusters used by cluster→map (higher = more detail)")
    ap.add_argument("--clean-direct", action="store_true",
                    help="use direct per-pixel palette quantize instead of cluster→map (noisier, faster)")
    ap.add_argument("--clean-cool-threshold", type=int, default=50,
                    help="minimum B-R bias a source cluster needs to map to a cool palette colour. "
                         "Higher = denim must be more strongly blue, prevents mild-blue eye/glasses regions "
                         "from mapping to indigo. Default 50 (denim ≈ 50+, eye area ≈ 30-45).")
    ap.add_argument("--clean-quality", type=int, default=80, help="JPEG quality (photo mode only)")
    ap.add_argument("--clean-contrast", type=float, default=1.0,
                    help="contrast boost before quantize (1.0 = none, >1.0 amplifies)")
    args = ap.parse_args(argv)

    halftone(
        args.src,
        args.dst,
        cell=args.cell,
        max_dot=args.max_dot,
        ink=hex_to_rgb(args.ink),
        paper=hex_to_rgb(args.paper),
        out_size=args.size,
        jitter=args.jitter,
        contrast=args.contrast,
        style=args.style,
    )

    if args.clean is not None:
        write_clean(
            args.src,
            args.clean,
            size=args.clean_size,
            mode=args.clean_mode,
            palette_name=args.clean_palette,
            bg_threshold=args.clean_bg_threshold,
            bg_saturation_max=args.clean_bg_saturation_max,
            bg_feather=args.clean_bg_feather,
            quality=args.clean_quality,
            contrast=args.clean_contrast,
            dither=args.clean_dither,
            presoften=args.clean_presoften,
            presoften_median=args.clean_presoften_median,
            postsoften_median=args.clean_postsoften_median,
            n_clusters=args.clean_clusters,
            direct_quantize=args.clean_direct,
            cool_threshold=args.clean_cool_threshold,
            block=args.clean_block,
            blocky_alpha=args.clean_blocky_alpha,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
