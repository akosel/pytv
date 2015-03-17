#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

$DIR/startplay.sh &
omxplayer -o hdmi "$1" < /tmp/cmd
