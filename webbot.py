from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit
from plebot import plebotMessage
import os
from flask import send_from_directory

app = Flask(__name__)
io = SocketIO(app)

@app.route('/Plebot/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('chat.html')


@io.on('sendMessage')
def send_message_handler(msg):
    print(input)
    emit('getMessage', msg, json=True)
    emit('getMessage', plebotMessage(str(msg)), json=True)

if __name__ == '__main__':
    io.run(app, debug=True)

