# -*- coding: utf-8 -*-

"""
brickify.palettes
---------------

This module contains the brick palette mappings.

Color mapping source;
 - http://www.brickjournal.com/files/PDFs/2010LEGOcolorpalette.pdf


    USAGE:
    $ brickify.palettes.bricks

See README for project details.
"""

from __future__ import division


BRICKS = {
    "solid": {
        "024": [0xFE, 0xC4, 0x01],
        "106": [0xE7, 0x64, 0x19],
        "021": [0xDE, 0x01, 0x0E],
        "221": [0xDE, 0x38, 0x8B],
        "023": [0x01, 0x58, 0xA8],
        "028": [0x01, 0x7C, 0x29],
        "119": [0x95, 0xB9, 0x0C],
        "192": [0x5C, 0x1D, 0x0D],
        "018": [0xD6, 0x73, 0x41],
        "001": [0xF4, 0xF4, 0xF4],
        "026": [0x02, 0x02, 0x02],
        "226": [0xFF, 0xFF, 0x99],
        "222": [0xEE, 0x9D, 0xC3],
        "212": [0x87, 0xC0, 0xEA],
        "037": [0x01, 0x96, 0x25],
        "005": [0xD9, 0xBB, 0x7C],
        "283": [0xF5, 0xC1, 0x89],
        "208": [0xE4, 0xE4, 0xDA],
        "191": [0xF4, 0x9B, 0x01],
        "124": [0x9C, 0x01, 0xC6],
        "102": [0x48, 0x8C, 0xC6],
        "135": [0x5F, 0x75, 0x8C],
        "151": [0x60, 0x82, 0x66],
        "138": [0x8D, 0x75, 0x53],
        "038": [0xA8, 0x3E, 0x16],
        "194": [0x9C, 0x92, 0x91],
        "154": [0x80, 0x09, 0x1C],
        "268": [0x2D, 0x16, 0x78],
        "140": [0x01, 0x26, 0x42],
        "141": [0x01, 0x35, 0x17],
        "312": [0xAA, 0x7E, 0x56],
        "199": [0x4D, 0x5E, 0x57],
        "308": [0x31, 0x10, 0x07],
    },
    "transparent": {
        "044": [0xF9, 0xEF, 0x69],
        "182": [0xEC, 0x76, 0x0E],
        "047": [0xE7, 0x66, 0x48],
        "041": [0xE0, 0x2A, 0x29],
        "113": [0xEE, 0x9D, 0xC3],
        "126": [0x9C, 0x95, 0xC7],
        "042": [0xB6, 0xE0, 0xEA],
        "043": [0x50, 0xB1, 0xE8],
        "143": [0xCE, 0xE3, 0xF6],
        "048": [0x63, 0xB2, 0x6E],
        "311": [0x99, 0xFF, 0x66],
        "049": [0xF1, 0xED, 0x5B],
        "111": [0xA6, 0x91, 0x82],
        "040": [0xEE, 0xEE, 0xEE],
    },
    "effects": {
        "131": [0x8D, 0x94, 0x96],
        "297": [0xAA, 0x7F, 0x2E],
        "148": [0x49, 0x3F, 0x3B],
        "294": [0xFE, 0xFC, 0xD5],
    },
    "mono": {"001": [0xF4, 0xF4, 0xF4], "026": [0x02, 0x02, 0x02]},
}


def extend_palette(palette, colors=256, rgb=3):
    """Extend palette colors to 256 rgb sets."""
    missing_colors = colors - len(palette) // rgb
    if missing_colors > 0:
        first_color = palette[:rgb]
        palette += first_color * missing_colors
    return palette[: colors * rgb]


def bricks():
    """Build flattened brick palettes."""
    return _flatten_palettes(BRICKS.copy())


def _flatten_palettes(palettes):
    """Convert palette mappings into color list."""
    flattened = {}
    palettes = _merge_palettes(palettes)
    for palette in palettes:
        flat = [i for sub in palettes[palette].values() for i in sub]
        flattened.update({palette: flat})
    return flattened


def _merge_palettes(palettes):
    """Build unified palette using all colors."""
    unified = {}
    for palette in palettes:
        for item in palettes[palette]:
            unified.update({item: palettes[palette][item]})
    palettes.update({"all": unified})
    return palettes
