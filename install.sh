#!/bin/bash

INSTALLOC="$HOME/.local/share/gnome-shell/extensions/desktop-wallpaper-slider"

rm -rf $INSTALLOC

mkdir -p $INSTALLOC

chown 
cp ./manager.py ./database.py ./run.py ./extension.js ./metadata.json ./requirements.txt $INSTALLOC

