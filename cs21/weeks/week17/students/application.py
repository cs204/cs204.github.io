import cs50
from flask import Flask, render_template
app = Flask(__name__)

db = cs50.SQL("sqlite:///students.db")


@app.route("/")
def index():
    факультет = "Слизерни"
    студенты = db.execute("SELECT имя, отчество, фамилия, рождение FROM студенты WHERE факультет=? ORDER BY фамилия, имя", факультет) 
    print(студенты[0]["имя"])
    return render_template("index.html", студенты=студенты)
