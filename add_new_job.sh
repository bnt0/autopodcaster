#!/bin/bash

script_name="record_stream.sh"
script_path=`pwd`/$script_name

(crontab -l 2>/dev/null; echo "0 16 * * 1-5 $script_path") | crontab -

# min (0-59) hour (0-23) day_of_month (1-31) month (1-12) day_of_week (0-6: sunday to saturday)
