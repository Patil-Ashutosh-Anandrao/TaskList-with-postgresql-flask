from flask import Flask
from flask import render_template
# from flask import psycopg2
from flask import request
from flask import redirect
from flask import url_for


# Import the getTaskList function from the db.py file. This function retrieves the task list from the database.
from db import getTaskList
from db import addTask

app = Flask(__name__)

# tasklist = [["walk Dog", True], ["Wash Dishes", False], ["Sleep", True], ["Study", True]]

# Call the getTaskList function to retrieve the task list from the database. Store the task list in the tasklist
# variable.
tasklist = getTaskList()


@app.route("/")
def home():
    tasklist = getTaskList()
    return render_template("tasklist.html", TaskList=tasklist)

@app.route("/add",methods=['POST'])
def add():
    taskName = request.form['taskName']
    dueDate = request.form['dueDate']
    addTask(taskName, dueDate)
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True, port=8000)

