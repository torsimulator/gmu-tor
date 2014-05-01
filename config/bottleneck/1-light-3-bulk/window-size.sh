#!/bin/bash

for i in $(seq 1 1 $1)
do
	scallion -i try1.xml
	grep "CIRCUIT, STREAM" data/scallion.log | cut -d ':' -f5 > data/window.log
	file="window-$i"
	zip "$file.zip" data/window.log
	rm  -r data/
done
