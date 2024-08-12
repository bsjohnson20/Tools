#!/bin/dash
find . -type f -exec bash -c 'echo /bin/bash' {} \; | sort -u | sed 's/^/Unique file extensions: ./'
