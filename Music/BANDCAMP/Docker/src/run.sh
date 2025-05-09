#!/usr/bin/bash

# entrypoint docker
# activate .venv
rm music.zip
mv ./src .
ls -a .
uv run main.py
# .venv/bin/python main.py

while true; do sleep 1000; done