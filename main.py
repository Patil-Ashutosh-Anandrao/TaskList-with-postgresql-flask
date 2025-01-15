from flask import Flask # Import the Flask class from the flask module.
from flask import render_template # Import the render_template function from the flask module.
# from flask import psycopg2
from flask import request # Import the request object from the flask module.
from flask import redirect # Import the redirect function from the flask module.
from flask import url_for # Import the url_for function from the flask module.


from db import getTaskList # Import the getTaskList function from the db.py file. This function retrieves the task list from the database.
from db import addTask # Import the addTask function from the db.py file. This function adds a new task to the database.
from db import updateTask # Import the updateTask function from the db.py file. This function updates an existing task in the database.
from db import deleteTask # Import the deleteTask function from the db.py file. This function deletes a task from the database.

# Create an instance of the Flask class and store it in the app variable.
app = Flask(__name__)

# tasklist = [["walk Dog", True], ["Wash Dishes", False], ["Sleep", True], ["Study", True]]

# Call the getTaskList function to retrieve the task list from the database. Store the task list in the tasklist
# variable.
tasklist = getTaskList()


@app.route("/")
def home():
    tasklist = getTaskList() # Call the getTaskList function to retrieve the task list from the database. Store the task list in the tasklist variable.
    return render_template("tasklist.html", TaskList=tasklist)  # Render the tasklist.html template and pass the tasklist variable to the template. 
                                                                # This variable will be used to display the task list on the web page. 
                                                                # The template is stored in the templates folder. The TaskList variable is used in the template to display the task list.


@app.route("/add",methods=['POST'])
def add():
    taskName = request.form['taskName']  # Retrieve the task name from the form data. The task name is stored in the taskName variable. 
    dueDate = request.form['dueDate'] # Retrieve the due date from the form data. The due date is stored in the dueDate variable. 
    addTask(taskName, dueDate) # Call the addTask function to add a new task to the database. Pass the task name and due date as arguments to the function. 
    return redirect(url_for('home')) # Redirect the user to the home route. The user will be redirected to the home page after adding a new task to the database. 


@app.route("/update",methods=['POST'])
def update():
    updatedtaskname = request.form['updateTask'] # Retrieve the updated task name from the form data. The updated task name is stored in the updatedtaskname variable. 
    id= request.form['id'] # Retrieve the task ID from the form data. The task ID is stored in the id variable.   
    button = request.form['saveOrDelete'] # Retrieve the value of the saveOrDelete button from the form data. The value is stored in the button variable. 

    if button=="save":
        updateTask(updatedtaskname, id) # Call the updateTask function to update an existing task in the database. Pass the updated task name and task ID as arguments to the function.

    elif button=="Delete":
        deleteTask(id) # Call the deleteTask function to delete a task from the database. Pass the task ID as an argument to the function.

    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True, port=8000)

