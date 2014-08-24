#!/bin/bash

grep "fg-download-complete" data/scallion.log|grep "327680" > temp.log
sed -e 's/^.*\(first bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > first_bytes_327680.log
sed -e 's/^.*\(bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > download_time_327680.log
#Rscript summarize.r


grep "fg-download-complete" data/scallion.log|grep "5242880" > temp.log
sed -e 's/^.*\(first bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > first_bytes_5242880.log
sed -e 's/^.*\(bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > download_time_5242880.log
#Rscript summarize.r
