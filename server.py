import os
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

@app.route("/onguard/")
@app.route("/")
def onguard():
    return render_template("index.html")

@app.route("/volon/")
def volon():
    os.system("python volume_on.py")

@socketio.on("operationkillall")
def killall_ops(data):
    os.system("python volume_off.py")
    os.system("python lad.py")

if __name__ == "__main__":
    socketio.run(app, host="192.168.0.129", debug=True)