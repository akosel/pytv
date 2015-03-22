#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Make the fifo file if it doesn't exist
if [ ! -f /tmp/cmd ]; then
  mkfifo /tmp/cmd
fi

# Create a file for managing play state
touch /tmp/playing

# Switch TV input to Pi hdmi
echo "as" | cec-client -s

# Start the movie
$DIR/startplay.sh &
omxplayer -o hdmi "$1" < /tmp/cmd

# Remove our playing file
rm /tmp/playing
