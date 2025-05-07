#!/bin/bash
uv sync
cp override_files/bandcamp-api/* .venv/lib/python3.11/site-packages/bandcamp_api/
uv run main.py