#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Wrong amount of arguments."
  exit 1
fi

echo "loading background image: file:///$1"

gsettings set org.gnome.desktop.background picture-uri $1
gsettings set org.gnome.desktop.background picture-uri-dark $1

