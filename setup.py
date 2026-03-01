#!/usr/bin/env python

from setuptools import setup

setup(
    name="brickify",
    version="1.0.0",
    author="René Slowenski",
    author_email="rene@slowenski.de",
    url="https://github.com/rene-slowenski/brickify",
    description="Make images look as if they are made out of 1x1 interlocking bricks",
    long_description=(
        "Brickify is a python program that takes a static image or"
        " gif and makes it so that it looks as if it was built "
        "out of interlocking bricks."
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
    ],
    license="MIT",
    packages=["brickify"],
    install_requires=["pillow", "click"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "brickify = brickify.cli:main",
        ],
    },
    package_data={
        "bricks": ["*.png"],
    },
    test_suite="nose.collector",
    tests_require=["nose"],
)
