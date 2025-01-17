#!/bin/bash

INSTALLOC="$HOME/.local/bin/desktop-wallpaper-slider"

rm -rf $INSTALLOC

mkdir $INSTALLOC

cp ./manager.py ./database.py ./run.py ./metadata.json ./requirements.txt $INSTALLOC
cp ./bg-slider "$HOME/.local/bin/"

