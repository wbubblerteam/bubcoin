from pathlib import Path
import renamer


COLOUR_REPLACES = {
        # Wbubbler dark
        '#F9AA4B': '#8ECEEA',
        # Wbubbler light
        '#F7931A': '#69BDDE',
    }
SVG_PATH = Path('src/qt/res/src/bitcoin.svg')

def main():
    print('Replacing colours in svg.')
    renamer.filereplace(SVG_PATH, COLOUR_REPLACES)
    print('Requires: inkscape, ImageMagick (convert).')
    print('icns sucks, do it yourself.')
    command = './relogoer.sh'
    print(command)
    os.system(command)
