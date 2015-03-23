# pytv
Lite GUI for playing videos on Raspberry Pi with omxplayer. I wrote this on a Raspberry Pi 2 running Raspbian. 
There are nice operating systems like OpenElec that are specialized for media, but I wanted the flexibility of Raspbian. Plus, I wanted to do all of the tinkering myself, because that's the main reason I bought the Pi. For tinkering. 

## Setup
Eventually, I will do a proper Makefile. For now, here are step-by-step instructions. From the terminal:

1. `git clone git@github.com:akosel/pytv.git`
2. `cd pytv`
2. `virtualenv venv`
3. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python app.py` or `gunicorn app:app` will start a local server. You can view it by opening your browser 
and typing http://[YOUR LOCAL IP]:8080. There might be nothing on the site until you add some video files. 
The video files need to be in a drive called /home/pi/usbdrv. You could also change the folder name. This should
really be configurable though, which is something I will do shortly.


#### Optional

* Install libcec if you want more control over the TV. This will only work if you have a CEC-capable TV. 
This tutorial is what I used for setting up my Raspbian Pi: http://www.raspberrypi.org/forums/viewtopic.php?f=29&t=70923

* Install nginx to keep a server running at all times. Much more reliable than Flask or standalone gunicorn. 
  1. `sudo apt-get install nginx`
  2. Follow instructions here to configure nginx: http://www.onurguzel.com/how-to-run-flask-applications-with-nginx-using-gunicorn/
  You can skip to step three.
  3. You'll also want to make an init script. Follow instructions here: http://www.onurguzel.com/managing-gunicorn-processes-with-supervisor/
  
* Map your usb drive to a local directory (/home/pi/usbdrv, for example). This tutorial is excellent: 
http://www.instructables.com/id/Mounting-a-USB-Thumb-Drive-with-the-Raspberry-Pi/step3/Set-up-a-mounting-point-for-the-USB-drive/
