from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr} !</h1>"

if __name__ == "__main__":
    app.run()