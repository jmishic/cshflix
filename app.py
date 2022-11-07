from flask import Flask, render_template, url_for, session
app = Flask(__name__)


@app.route("/testing")
def netflix():
    return render_template("testing.html")


@app.route("/")
def cshflix():
    return render_template("theater.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")
