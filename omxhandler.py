import os
import subprocess

cwd = os.getcwd()

def start():
    subprocess.Popen([os.path.join(cwd, 'commands/play.sh'), '/home/pi/usbdrv/Interstellar_(2014)_720p_BluRay_[G2G.fm].mp4'])

def forward():
    subprocess.call([os.path.join(cwd, 'commands/omxcmd.sh'), '\x1B[C'])

def rewind():
    subprocess.call([os.path.join(cwd, 'commands/omxcmd.sh'), '\x1B[D'])

def toggle_play():
    subprocess.call([os.path.join(cwd, 'commands/omxcmd.sh'), 'p'])
