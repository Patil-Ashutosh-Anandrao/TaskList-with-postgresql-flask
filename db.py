# To use psycopg2 for interacting with a PostgreSQL database in your Flask application, you need to import the
# library and establish a connection to your database.
import psycopg2

# Define the connection string to connect to the PostgreSQL database. The connection string contains the database name,
db_name = "TaskListDB"
db_user = "tasklist_user"
db_pw = "4367"
db_host = "localhost"
db_port = 5432


def getTaskList():

    # Connect to the database using the connection string provided in the previous step and store the connection in a
    # variable.
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host, port=db_port)

    # Create a cursor object using the connection object. The cursor object is used to interact
    # with the database.
    cur = conn.cursor()

    # Execute a query to select all the records from the task_list table.
    cur.execute('SELECT id, task_name, is_done FROM public."TaskList"')

    #Fetch all the records from the task_list table and store them in a variable.
    tasklist = cur.fetchall()

    # Close the cursor object.
    cur.close()

    # Close the connection object.
    conn.close()

    # Return the tasklist variable.
    return tasklist


def addTask(name,date):
    conn=psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host, port=db_port)
    cur=conn.cursor()
    cur.execute('INSERT INTO public."TaskList"(task_name,due_date)values(\'%s\',\'%s\');commit;'%(name, date))
    cur.close
    conn.close



def updateTask(name,id):
    conn=psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host, port=db_port)
    cur=conn.cursor()
    cur.execute('UPDATE public."TaskList" SET task_name=\'%s\' WHERE id=%s;' % (name, id))
    conn.commit()
    cur.close
    conn.close



def deleteTask(id):
    conn=psycopg2.connect(dbname=db_name, user=db_user, password=db_pw, host=db_host, port=db_port)
    cur=conn.cursor()
    cur.execute('DELETE FROM public."TaskList" WHERE id=%s;' % (id))
    conn.commit()
    cur.close
    conn.close