from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
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

def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS public.devops_users
            (
                id integer NOT NULL DEFAULT nextval('devops_users_id_seq'::regclass),
                username text COLLATE pg_catalog."default" NOT NULL,
                password text COLLATE pg_catalog."default" NOT NULL,
                CONSTRAINT devops_users_pkey PRIMARY KEY (id)
            ) """)
        conn.commit()
        cur.close() 
        return 1
    except:
        return 0
    
def create_user(conn, usr, passwd):
    try:
        cur = conn.cursor()
        sql = "INSERT into devops_users(username, password) VALUES ('"+usr+"', '"+passwd+"');"
        cur.execute(sql)
        conn.commit()
        cur.close()
        return "OK", 1
    except:
        return " ", 0


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        conn = connection_database()
        answer = create_user(conn, user, password)
        conn.close()
        if answer == "OK":
            return redirect(url_for("user", usr=user))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr} ! Data has been send</h1>"

if __name__ == "__main__":
    app.run()