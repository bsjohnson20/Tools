#!/bin/dash
sudo apt-get purge pulseaudio
sudo apt-get clean && sudo apt-get autoremove
rm -r ~/.pulse ~/.asound* ~/.pulse-cookie ~/.config/pulse
sudo apt-get install pulseaudio
sudo alsa force-reload
pavucontrol
