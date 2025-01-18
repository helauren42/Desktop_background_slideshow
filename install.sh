#!/bin/bash

echo "Installing bg-slideshow"

INSTALLOC="$HOME/.local/bin/.app-bg-slideshow/"
BINLOC="$HOME/.local/bin/"

rm -rf $INSTALLOC

mkdir -p $BINLOC
mkdir $INSTALLOC

cp ./manager.py ./bg-slideshow.py ./database.py ./requirements.txt ./uninstall.sh $INSTALLOC
cp ./bg-slideshow ./bg-slideshow.sh "$HOME/.local/bin/"

chown $USER:$USER $INSTALLOC
chown $USER:$USER $INSTALLOC/*

echo "Installation done"
