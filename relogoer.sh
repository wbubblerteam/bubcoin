#!/bin/bash
set -x

cd src/qt/res/icons
# Render svg to png with Inkscape
inkscape --export-type="png" --export-dpi=72 -w 1024 -h 1024 --export-filename="bubcoin.png" "../src/bubcoin.svg"
inkscape --export-type="png" --export-dpi=72 -w 1024 -h 1024 --export-filename="bubcoin_testnet.png" "../src/bubcoin_testnet.svg"
# Use Magick to create ico here with the same sizes, omit antiquitated color depths
convert "bubcoin.png" -define icon:auto-resize=48,32,16,256 "bubcoin.ico"
convert "bubcoin_testnet.png" -define icon:auto-resize=16,32,48,256 "bubcoin_testnet.ico"
cd ../../../../share/pixmaps
PNG_SRC=../../src/qt/res/icons/bubcoin.png
# Likewise, make this other ico
convert $PNG_SRC -define icon:auto-resize=256,64,48,32,20,16 "bubcoin.ico"
# Generate assorted png's and xpm's
for size in 16 32 64 128 256
do
    convert $PNG_SRC -resize $size "bubcoin$size.png"
    convert $PNG_SRC -resize $size "bubcoin$size.xpm"
done
