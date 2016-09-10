#!/bin/sh

playlist_url="https://www.youtube.com/playlist?list=PL_m5i4Bl8okmioycXqux5BuIhffO9yLo3"

date=`date`

output_dir=$HOME/autopodcaster/youtube/
mkdir -p $output_dir
cd $output_dir

youtube-dl --audio-format mp3 --extract-audio --date $date $playlist_url
