#!/bin/bash

INSTALLOC="$HOME/.local/bin/.app-bg-slideshow"
DIR_BIN="$HOME/.local/bin/bg-slideshow"
DIR_SCRIPT="$HOME/.local/bin/bg-slideshow.sh"

echo "removing bg-slideshow"

res=0

if ps aux | grep -v grep | grep -q 'bg-slideshow'; then
    echo "stopping current running instance of bg-slideshow"
    bg-slideshow -stop
fi

if test ! -d $INSTALLOC; then
    echo "Error: can not find application directory"
    res=1
else
    rm -rf $INSTALLOC
fi

if test ! -f $DIR_BIN; then
    echo "Error: can not find binary"
    res=1
else
    rm $DIR_BIN
fi

if test ! -f $DIR_SCRIPT; then
    echo "Error: can not find application's shell script"
    res=1
else
    rm $DIR_SCRIPT
fi

if test $res -eq 0; then
    echo "uninstall successful"
else
    echo "uninstall failed"
fi

