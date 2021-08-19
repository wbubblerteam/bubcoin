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
        # Wbubbler light beige
        '#F9AA4B': '#F4DFCC',
        # Wbubbler dark beige
        '#F7931A': '#B29E8B',
    }
SVG_PATH = Path('src/qt/res/src/bitcoin.svg')
SVG_PATH_TESTNET = SVG_PATH.with_name('bitcoin_testnet.svg')


def main():
    print('Copying svg for testnet icon.')
    shutil.copy(SVG_PATH, SVG_PATH_TESTNET)
    print("Replacing colours in svg's.")
    renamer.filereplace(SVG_PATH, COLOUR_REPLACES)
    renamer.filereplace(SVG_PATH_TESTNET, COLOUR_REPLACES_TESTNET)
    print('Requires: inkscape, ImageMagick (convert).')
    print('icns sucks, do it yourself.')
    command = './relogoer.sh'
    print(command)
    os.system(command)


if __name__ == '__main__':
    main()
