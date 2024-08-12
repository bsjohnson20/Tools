#!/bin/dash
rclone sync /media/lunachocken/external_dr/Coursework/ remote:SSD_backup --progress --order-by size,descending --update
