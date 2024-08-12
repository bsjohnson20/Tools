#!/bin/dash
directory="./TestFolder"
directoryDisabled="./TestDisabledFolder"

if [ -d "$directory" ]; then
     echo Disabled Folder!
     mv $directory $directoryDisabled
     # if body
elif [ -d "$directoryDisabled" ]; then
     echo Enabled Folder
     mv $directoryDisabled $directory
     # else if body
else
echo hello
     # else body


fi

