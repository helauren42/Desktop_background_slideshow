#!/bin/bash

echo "Installing bg-slideshow"
echo "This program requires that you have python3 with typing module, a c compiler and the shc command installed"

if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed please install it first"
    exit 1
fi

if ! command -v gcc &> /dev/null && ! command -v clang &> /dev/null; then
    echo "Error: No C compiler (gcc or clang) is installed. Please install one."
    exit 1
fi

if ! command -v shc &> /dev/null; then
    echo "Error: shc is not installed on your device, please install shc first"
    exit 1
fi

INSTALLOC="$HOME/.local/bin/.app-bg-slideshow/"
BINLOC="$HOME/.local/bin/"

rm -rf $INSTALLOC

mkdir -p $BINLOC
mkdir $INSTALLOC

cp ./manager.py ./bg-slideshow.py ./database.py ./uninstall.sh $INSTALLOC
cp ./bg-slideshow ./bg-slideshow.sh "$HOME/.local/bin/"

chown $USER:$USER $INSTALLOC
chown $USER:$USER $INSTALLOC/*

echo "Installation completed succesfully"
