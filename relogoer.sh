#!/bin/bash
set -x

root_dir=$(pwd)
src_dir=$root_dir/src
icons_dir=$src_dir/qt/res/icons
pixmaps_dir=$root_dir/share/pixmaps

cd $icons_dir

# Render svg to png with Inkscape
inkscape --export-type="png" --export-dpi=72 -w 1024 -h 1024 --export-filename="bitcoin.png" "$src_dir/bitcoin.svg"
inkscape --export-type="png" --export-dpi=72 -w 1024 -h 1024 --export-filename="bitcoin_testnet.png" "$src_dir/bitcoin_testnet.svg"

# Use Magick to create ico here with the same sizes, omit antiquitated color depths
convert "bitcoin.png" -define icon:auto-resize=48,32,16,256 "bitcoin.ico"
convert "bitcoin_testnet.png" -define icon:auto-resize=16,32,48,256 "bitcoin_testnet.ico"

cd $pixmaps_dir

png_src=$icons_dir/bitcoin.png
# Likewise, make this other ico
convert $png_src -define icon:auto-resize=256,64,48,32,20,16 "bitcoin.ico"

# Generate assorted png's and xpm's
for size in 16 32 64 128 256
do
    convert $png_src -resize $size "bitcoin$size.png"

    size_underscores=$(python3 -c "print('_' * len('$size'))")
    convert $png_src -resize $size "bitcoin$size_underscores.xpm"
    mv "bitcoin$size_underscores.xpm" "bitcoin$size.xpm"
done
