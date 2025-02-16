#!/bin/bash

APP_PATH="$HOME/.local/appman/apps/bg-slideshow"
SCRIPT_PATH="$HOME/.local/appman/run/bg-slideshow.sh"

echo "removing bg-slideshow"

res=0

if ps aux | grep -v grep | grep -q 'bg-slideshow.py'; then
    echo "killing current running instance of bg-slideshow"
    pkill bg-slideshow.py
fi

if test ! -d $APP_PATH; then
    echo "Error: can not find application directory"
    res=1
else
    rm -rf $APP_PATH
fi

if test ! -f $SCRIPT_PATH; then
    echo "Error: can not find application's shell script"
    res=1
else
    rm $SCRIPT_PATH
fi

if test $res -eq 0; then
    echo "uninstall successful"
else
    echo "uninstall failed"
fi
