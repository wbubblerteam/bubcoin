#!/usr/bin/env python3.9

import os
import shutil
from pathlib import Path

import renamer


COLOUR_REPLACES = {
        # Wbubbler light blue
        '#F9AA4B': '#8ECEEA',
        # Wbubbler dark blue
        '#F7931A': '#69BDDE',
    }
COLOUR_REPLACES_TESTNET = {
        # Wbubbler medium red
        '#F9AA4B': '#AB3342',
        # Wbubbler dark red
        '#F7931A': '#802A3A',
    }
SVG_PATH = Path('src/qt/res/src/bitcoin.svg')
SVG_PATH_TESTNET = SVG_PATH.with_name('bitcoin_testnet.svg')


def main():
    print('Copying svg for testnet icon.')
    shutil.copy(SVG_PATH, SVG_PATH_TESTNET)
    print("Replacing colours in svg's.")
    renamer.filereplace(SVG_PATH, mapping=COLOUR_REPLACES)
    renamer.filereplace(SVG_PATH_TESTNET, mapping=COLOUR_REPLACES_TESTNET)
    print('Requires: inkscape, ImageMagick (convert).')
    print('icns sucks, do it yourself.')
    command = './relogoer.sh'
    print(command)
    os.system(command)


if __name__ == '__main__':
    main()
