import os
import subprocess

cwd = os.getcwd()
omx = os.path.join(cwd, 'commands/omxcmd.sh')

def start(path):
    subprocess.Popen([os.path.join(cwd, 'commands/play.sh'), path])

def forward():
    subprocess.call([omx, '\x1B[C'])

def rewind():
    subprocess.call([omx, '\x1B[D'])

def toggle_play():
    subprocess.call([omx, 'p'])

def quit():
    subprocess.call([omx, 'q'])
