#!/usr/bin/env python3
"""Export one approved illustration as RGB JPG or PNG and verify geometry."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_ratio(value: str) -> float:
    try:
        width, height = value.split(":", 1)
        ratio = float(width) / float(height)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError("Ratio must look like 2:3") from exc
    if ratio <= 0:
        raise argparse.ArgumentTypeError("Ratio must be positive")
    return ratio


def flatten_rgb(image: Image.Image, ground: str) -> Image.Image:
    if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
        rgba = image.convert("RGBA")
        canvas = Image.new("RGB", rgba.size, ground)
        canvas.paste(rgba, mask=rgba.getchannel("A"))
        return canvas
    return image.convert("RGB")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--ratio", type=parse_ratio, help="Expected ratio, e.g. 2:3")
    parser.add_argument("--ratio-tolerance", type=float, default=0.01)
    parser.add_argument("--min-long-edge", type=int, default=1536)
    parser.add_argument("--ground", default="#D9F1EE")
    parser.add_argument("--quality", type=int, default=94, choices=range(1, 96))
    args = parser.parse_args()

    with Image.open(args.source) as source_image:
        image = flatten_rgb(source_image, args.ground)

    width, height = image.size
    if max(width, height) < args.min_long_edge:
        raise ValueError(
            f"Long edge is {max(width, height)} px; expected at least {args.min_long_edge} px."
        )
    if args.ratio is not None:
        actual = width / height
        relative_error = abs(actual - args.ratio) / args.ratio
        if relative_error > args.ratio_tolerance:
            raise ValueError(
                f"Actual ratio {width}:{height} ({actual:.4f}) does not match "
                f"expected {args.ratio:.4f} within {args.ratio_tolerance:.1%}."
            )

    args.destination.parent.mkdir(parents=True, exist_ok=True)
    suffix = args.destination.suffix.lower()
    if suffix in (".jpg", ".jpeg"):
        image.save(args.destination, "JPEG", quality=args.quality, subsampling=0, optimize=True)
    elif suffix == ".png":
        image.save(args.destination, "PNG", optimize=True)
    else:
        raise ValueError("Destination extension must be .jpg, .jpeg, or .png")

    print(f"Exported {args.destination} — {width}x{height}, RGB")


if __name__ == "__main__":
    main()
