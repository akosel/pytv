import os
import subprocess
import flask
import omxhandler

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

@app.route('/play')
def play():
    omxhandler.start()
    return 'done'

@app.route('/cmd/<cmd>')
def key(cmd):
    if cmd == 'play' or cmd == 'pause':
        omxhandler.toggle_play()
    elif cmd == 'rewind':
        omxhandler.rewind()
    elif cmd == 'forward':
        omxhandler.forward()

    return 'done'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
