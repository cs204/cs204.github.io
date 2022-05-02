from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/регистрация", methods=["POST"])
def регистрация():
    имя = request.form.get("имя")
    return render_template("result.html", имя = имя)

