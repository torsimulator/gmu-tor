#!/bin/bash

grep "download-complete" data/scallion.log|grep "lightfileclient" > temp.log
sed -e 's/^.*\(first bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > first_bytes_327680.log
sed -e 's/^.*\(bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > download_time_327680.log
#Rscript summarize.r

grep "download-complete" data/scallion.log|grep "bulkfileclient" > temp.log
sed -e 's/^.*\(first bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > first_bytes_5242880.log
sed -e 's/^.*\(bytes in [^ ]*\).*$/\1/' temp.log | tr ' ' '\n' | sed -rne "/([0-9])/P" > download_time_5242880.log
#Rscript summarize.r
