#!/bin/bash

grep  "download-complete" data/scallion.log > temp.log
sed -e 's/^.*\(first bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > first_bytes.log
sed -e 's/^.*\(bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > download_time.log
#Rscript summarize.r
