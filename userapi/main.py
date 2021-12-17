from flask import Flask, render_template, request, url_for, redirect
import psycopg2

hostname = 'localhost'
mydb = 'DevOps'
username = 'postgres'
passwrd = "ECE2021"
port_id = '5432'

app = Flask(__name__)


def connection_database():
    try:
        conn = psycopg2.connect(host=hostname,database=mydb,user=username,password=passwrd,port=port_id)  
        return conn , 1
    except:
        return " " , 0    
    
def create_todo(conn, todo):
    try:
        cur = conn.cursor()
        sql = "INSERT into devops_users(todo) VALUES ('"+todo+"');"
        cur.execute(sql)
        conn.commit()
        cur.close()
        return "OK", 1
    except:
        return " ", 0

def delete_todo(conn, todo):
    try:
        cur = conn.cursor()
        sql = "DELETE from devops_users WHERE todo='"+todo+"'"
        cur.execute(sql)
        conn.commit()
        cur.close()
        return "OK", 1
    except:
        return " ", 0

def get_todo(conn):
    try:
        cur = conn.cursor()
        sql = "Select todo from devops_users ORDER BY id ASC "
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        return rows, 1
    except:
        return " ", 0

def update_todo(conn, todo, newTodo):
    try:
        cur = conn.cursor()
        sql = "UPDATE devops_users SET todo='"+newTodo+"' WHERE todo='"+todo+"'"
        cur.execute(sql)
        conn.commit()
        cur.close()
        return "OK", 1
    except:
        return " ", 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/todo", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        todo = request.form["todo"]
        conn, stringValue = connection_database()
        msg, value = create_todo(conn, todo)
        return redirect(url_for("todoList", newTodo=todo))
    else:
        return render_template("addTodo.html")

@app.route("/<newTodo>")
def todoList(newTodo):
    return render_template("todoAdded.html")

@app.route("/todoList")
def myTodoList():
    conn, stringValue = connection_database()
    rows, value = get_todo(conn)
    return render_template("todoList.html", values=rows)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')