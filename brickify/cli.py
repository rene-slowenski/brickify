"""Command line interface to Brickify"""

import click
import brickify
from brickify import palettes


@click.command()
@click.argument(
    "image",
    required=True,
    type=click.Path(dir_okay=False, exists=True, resolve_path=True),
)
@click.argument(
    "output", default=None, required=False, type=click.Path(resolve_path=True)
)
@click.option(
    "--size",
    default=None,
    type=int,
    help="Number of bricks the longest side of the brickified image should have.",
)
@click.option(
    "--dither/--no-dither",
    default=False,
    help="Use dither algorithm to spread the color approximation error.",
)
@click.option(
    "--palette",
    default=None,
    type=click.Choice(palettes.bricks().keys()),
    help="Palette to use based on real brick colors.",
)
def main(image, output, size, palette, dither):
    """Brickify an image!"""
    brickify.main(
        image, output_path=output, size=size, palette_mode=palette, dither=dither
    )
