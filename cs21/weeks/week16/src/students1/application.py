from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("записи") is None:
        session["записи"] = []
    if request.method == "POST":
        запись = request.form.get("запись")
        session["записи"].append(запись)

    return render_template("index.html", записи = session["записи"])

