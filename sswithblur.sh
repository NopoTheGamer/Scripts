#!/usr/bin/env bash
coords1=$(slop)
coords2=$(slop)
region=$(echo ${coords2} | cut -d "+" -f 1)
coord1x=$(echo ${coords1} | cut -d "+" -f 2)
coord1y=$(echo ${coords1} | cut -d "+" -f 3)
coord2x=$(echo ${coords2} | cut -d "+" -f 2)
coord2y=$(echo ${coords2} | cut -d "+" -f 3)
let finalX="$coord2x-$coord1x"
let finalY="$coord2y-$coord1y"
maim -g ${coords1} -u | magick - -region "${region}+${finalX}+${finalY}" -blur 0x7 - | xclip -selection clipboard -t image/png -i
