#!/bin/sh
N=$1
len=`cat data/hightemp.txt | wc -l`
div=$((len/N))
split -l $div data/hightemp.txt	./work/x