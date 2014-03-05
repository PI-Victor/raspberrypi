#!/usr/bin/env bash

#search and kill every PID that has python rbpi.py

while true; do
   #find all processes atributed to python rbpi.py and kill them
    for i in `ps -ef | egrep "python ./rbpi.py" | awk '{print $2}'`; do echo ${i} && kill -9 ${i}; done
    nohup ./rbpi.py > bot.log 2>&1&
    read -p 'Restart the session?'
    sleep 5
done
