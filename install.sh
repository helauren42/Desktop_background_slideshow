#!/bin/bash

INSTALLOC="$HOME/.local/bin/.app-bg-slideshow/"

rm -rf $INSTALLOC

mkdir $INSTALLOC

cp ./manager.py ./bg-slideshow.py ./database.py ./requirements.txt ./uninstall.sh $INSTALLOC
cp ./bg-slideshow ./bg-slideshow.sh "$HOME/.local/bin/"

chown $USER:$USER $INSTALLOC
chown $USER:$USER $INSTALLOC/*
