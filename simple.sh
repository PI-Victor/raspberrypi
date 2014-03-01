#!/usr/bin/env bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
 
while true; do
    read -p `echo -e "Restart:\n"`
    service uwsgi restart

done