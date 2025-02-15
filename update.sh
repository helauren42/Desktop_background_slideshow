#!/bin/bash

echo "Updating bg-slideshow"

APP_PATH="$HOME/.local/appman/apps/bg-slideshow/"
BINLOC="$HOME/.local/appman/run/"

cp ./manager.py ./bg-slideshow.py ./database.py ./uninstall.sh $APP_PATH
cp ./bg-slideshow.sh $BINLOC/

echo "Update completed"
