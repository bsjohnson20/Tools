#!/bin/bash
find . | xargs -I{} sha256sum {} >> hashes.txt
cut -d ' ' -f 1 hashes.txt | sort | uniq -d > dupes.txt
cat dupes.txt
