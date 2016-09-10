#!/bin/sh

date=`date +"%Y_%a_%b_%d_%H%M%P"`

url=http://online.jazzy.hu/stream/1/
output_filename=track.${date}

duration=200               # duration of show in seconds

output_dir=/home/balint/autopodcaster/onkenyes/
mkdir -p $output_dir
cd $output_dir

streamripper $url -d $output_dir -l $duration -a $output_filename -o always
