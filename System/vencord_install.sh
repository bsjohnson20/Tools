#!/bin/dash
sh -c "$(curl -sS https://raw.githubusercontent.com/Vendicated/VencordInstaller/main/install.sh)"
killall Discord
flatpak run com.discordapp.Discord &
disown
