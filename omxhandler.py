import os
import subprocess

cwd = os.getcwd()
omx = os.path.join(cwd, 'commands/omxcmd.sh')

def start(path):
    subprocess.Popen([os.path.join(cwd, 'commands/play.sh'), path])

def forward():
    subprocess.call([omx, '\x1B[C'])

def forward_big():
    subprocess.call([omx, '\x1B[A'])

def rewind():
    subprocess.call([omx, '\x1B[D'])

def rewind_big():
    subprocess.call([omx, '\x1B[B'])

def toggle_play():
    subprocess.call([omx, 'p'])

def volume_up():
    subprocess.call([omx, '+'])

def volume_down():
    subprocess.call([omx, '-'])

def quit():
    subprocess.call(['rm', '/tmp/playing'])
    subprocess.call([omx, 'q'])

# Dictionary of commands for use in app.py
commandDict = {
    'play': toggle_play,
    'pause': toggle_play,
    'rewind': rewind,
    'rewind_big': rewind_big,
    'forward': forward,
    'forward_big': forward_big,
    'volume_up': volume_up,
    'volume_down': volume_down,
    'quit': quit
}
