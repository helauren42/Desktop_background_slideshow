#!/bin/bash

INSTALLOC="$HOME/.local/bin/desktop-wallpaper-slider/"

rm -rf $INSTALLOC

mkdir $INSTALLOC

cp ./manager.py ./run.py ./database.py ./requirements.txt ./uninstall.sh $INSTALLOC
cp ./bg-slideshow ./bg-slideshow.sh "$HOME/.local/bin/"

chown $USER:$USER $INSTALLOC
chown $USER:$USER $INSTALLOC/*
