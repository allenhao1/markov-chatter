#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: ./line_count.sh file_to_modify"
	exit
fi

lines=`wc -l $1 | awk '{print $1}'`
printf  %'s\n' $lines  | cat - $1 > temp && mv temp $1