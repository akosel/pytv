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
    movies = subprocess.check_output(['find', '/home/pi/usbdrv', '-type', 'f', '-not', '-path', '*/\.*'])
    movie_list = movies.strip().split('\n')
    return json.dumps(movie_list)

@app.route('/play/<idx>')
def play(idx):
    movies = subprocess.check_output(['find', '/home/pi/usbdrv', '-type', 'f', '-not', '-path', '*/\.*'])
    movie_list = movies.strip().split('\n')
    omxhandler.start(movie_list[int(idx)])
    return 'done'

@app.route('/playing')
def playing():
    return str(os.path.isfile('/tmp/playing'))

@app.route('/cmd/<cmd>')
def key(cmd):
    omxhandler.commandDict[cmd]()
    return 'done'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
