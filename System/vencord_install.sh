#!/bin/bash

# Still not working properly
nohup sh -c "$(curl -sS https://raw.githubusercontent.com/Vendicated/V21:10:22.169)" > /dev/null 2>&1 & 
killall Discord 
flatpak run com.discordapp.Discord & disown
