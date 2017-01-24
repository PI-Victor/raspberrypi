#!/usr/bin/env bash

while true; do
    ps -ef | grep rpimon.py | grep -v grep |grep -v emacs| wc -l
    sleep 5
done
