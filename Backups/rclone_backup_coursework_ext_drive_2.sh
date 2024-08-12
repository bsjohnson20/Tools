#!/bin/dash
rclone copy /media/lunachocken/external_dr/Coursework/ remote:SSD_backup --progress --order-by size,ascending --update
