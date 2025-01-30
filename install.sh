#!/bin/bash

echo "Installing bg-slideshow"

APP_PATH="$HOME/.local/appman/apps/bg-slideshow/"
BINLOC="$HOME/.local/appman/bin/"

mkdir -p $BINLOC
mkdir $APP_PATH
chmod u+x *.sh

cp ./metadata.json ./manager.py ./bg-slideshow.py ./database.py ./uninstall.sh $APP_PATH
cp ./bg-slideshow.sh "$BINLOC/"

chown $USER:$USER $APP_PATH

echo "Installation completed"
