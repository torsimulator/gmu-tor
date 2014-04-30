#!/bin/bash

grep "CIRCUIT," data/scallion.log > data/window.log
zip window-log.zip data/window.log
