#!/bin/bash

# Get the script's filename
script_filename=$(basename "$0")

# Get the directory of the script
script_dir=$(dirname "$(readlink -f "$0")")

# List all script files in the same directory (excluding the current script)
script_files=$(ls "$script_dir" | grep -E '\.sh$' | grep -v "$script_filename")

# Kill processes corresponding to script files
if [ -n "$script_files" ]; then
    echo "Killing processes corresponding to script files..."
    pkill -f "$script_files"
    echo "Processes killed."
else
    echo "No other processes found corresponding to script files."
fi

