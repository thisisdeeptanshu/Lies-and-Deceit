import os
from flask import Flask, redirect, render_template, url_for
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
    return redirect(url_for("onguard"))

@app.route("/help/")
def help():
    return "help"

@socketio.on("operationkillall")
def killall_ops(data):
    os.system("python volume_off.py")
    os.system("python lad.py")

if __name__ == "__main__":
    socketio.run(app, host="69420youriphere666333", debug=True)
