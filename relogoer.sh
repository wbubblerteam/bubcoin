#!/bin/bash
set -x

cd src/qt/res/icons
# Render svg to png with Inkscape
inkscape --export-type="png" --export-dpi=72 -w 1024 -h 1024 --export-filename="bitcoin.png" "../src/bitcoin.svg"
inkscape --export-type="png" --export-dpi=72 -w 1024 -h 1024 --export-filename="bitcoin_testnet.png" "../src/bitcoin_testnet.svg"
# Use Magick to create ico here with the same sizes, omit antiquitated color depths
convert "bitcoin.png" -define icon:auto-resize=48,32,16,256 "bitcoin.ico"
convert "bitcoin_testnet.png" -define icon:auto-resize=16,32,48,256 "bitcoin_testnet.ico"
cd ../../../../share/pixmaps
PNG_SRC=../../src/qt/res/icons
# Likewise, make this other ico
convert $PNG_SRC -define icon:auto-resize=256,64,48,32,20,16 "bitcoin.ico"
# Generate assorted png's and xpm's
for size in 16 32 64 128 256
do
    convert $PNG_SRC -resize $size "bitcoin$size.png"
    convert $PNG_SRC -resize $size "bitcoin$size.xpm"
done
