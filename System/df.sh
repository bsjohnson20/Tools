#!/bin/dash
i=0
while [ $i -le 100 ]
do
	clear && df
	i++
	sleep 1
done
