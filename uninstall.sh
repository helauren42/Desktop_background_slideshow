#!/bin/bash

INSTALLOC="$HOME/.local/bin/.app-bg-slideshow"

bg-slideshow -stop

rm "$HOME/.local/bin/bg-slideshow"

rm -rf $INSTALLOC
