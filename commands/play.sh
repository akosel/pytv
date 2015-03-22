#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Make the fifo file if it doesn't exist
if [ ! -f /tmp/cmd ]; then
  mkfifo /tmp/cmd
fi

echo "as" | cec-client -s
touch /tmp/playing
# Start the movie
$DIR/startplay.sh &
omxplayer -o hdmi "$1" < /tmp/cmd
rm /tmp/playing
