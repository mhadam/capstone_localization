#!/bin/bash

# unbuffer ./pip_sense l l |  while read LINE; do echo "$LINE" | grep -P "TX:02003."; done | tee log.txt
date1=$(date +"%y%m%d-%H%M%S")
echo "$date1.txt"
# read -p "Describe something" RESP
mkdir -p logs
touch "./logs/$date1.txt"
chown -R pi:pi "./logs/"
unbuffer ./pip_sense l l | while read LINE; do echo "$LINE" ; done | tee "logs/$date1.txt"
