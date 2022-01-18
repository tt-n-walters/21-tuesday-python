from flask import Flask, request

app = Flask(__name__)


logged_on = False
correct_user = "bob"
correct_password = "techtalents"

@app.route("/")
def get_index():
    if logged_on:
        return "Successful. Hello world"
    else:
        return "Not logged in. Blocked. Go away."


@app.route("/login", methods=["GET", "POST"])
def login():
    global logged_on
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print("Login attempt with", repr(username), "and", repr(password))
        if username == correct_user:
            if password == correct_password:
                logged_on = True
                return "Logged in successfully."
            else:
                return "Password incorrect."
        else:
            return "User not found."
            
    elif request.method == "GET":
        with open("login.html", "r") as file:
            return file.read()


@app.route("/logout")
def logout():
    global logged_on
    if logged_on:
        logged_on = False
        return "Successfully logged out."
    else:
        return "You are not logged in."
