from flask import Flask
from flask import render_template

app = Flask(__name__)

tasklist = [["walk Dog", True], ["Wash Dishes", False], ["Sleep", True]]


@app.route("/")
def home():
    return render_template("tasklist.html", TaskList=tasklist)


app.run()
