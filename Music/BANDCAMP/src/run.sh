#!/usr/bin/bash

# entrypoint docker
# activate .venv
mv ./src .
ls -a .
source .venv/bin/activate
.venv/bin/python main.py

while true; do sleep 1000; done