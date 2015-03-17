import os
import subprocess
import flask
import omxhandler
import json

app = flask.Flask(__name__)
cwd = os.getcwd()

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/on')
def on():
    subprocess.call([os.path.join(cwd, 'commands/on.sh')])
    return 'done'

@app.route('/off')
def off():
    subprocess.call([os.path.join(cwd, 'commands/off.sh')])
    return 'done'

@app.route('/movies')
def movies():
    movies = subprocess.check_output(['find', '/home/pi/usbdrv', '-type', 'f', '-not', '-path', '"*/\.*"'])
    movie_list = movies.strip().split('\n')
    return json.dumps(movie_list)

@app.route('/play/<idx>')
def play(idx):
    #path = '/home/pi/usbdrv/Interstellar_(2014)_720p_BluRay_[G2G.fm].mp4'
    movies = subprocess.check_output(['find', '/home/pi/usbdrv', '-type', 'f', '-not', '-path', '"*/\.*"'])
    movie_list = movies.strip().split('\n')
    omxhandler.start(movie_list[int(idx)])
    return 'done'

@app.route('/cmd/<cmd>')
def key(cmd):
    if cmd == 'play' or cmd == 'pause':
        omxhandler.toggle_play()
    elif cmd == 'rewind':
        omxhandler.rewind()
    elif cmd == 'forward':
        omxhandler.forward()
    elif cmd == 'quit':
        omxhandler.quit()

    return 'done'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
