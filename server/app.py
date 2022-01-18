from flask import Flask, request
import os


folder_name = os.path.dirname(os.path.abspath(__file__)) + "/"
app = Flask(__name__)


logged_on = False


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def __repr__(self):
        return repr("User with name: " + repr(self.name))
    
    def check_name(self, name):
        if name == self.name:
            return True
        else:
            return False

    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False

    def check(self, name, password):
        """
            Checks username and password. Returns an int code depending.
            0 -> Successful login
            1 -> Incorrect password
            2 -> Invalid username
        """
        if self.check_name(name):
            if self.check_password(password):
                return 0
            else:
                return 1
        else:
            return 2


users = []

def register(name, password):
    for existing_user in users:
        print("Checking", existing_user)
        if existing_user.check_name(name):
            print("User with name", name, "already exists.")
            return

    new_user = User(name, password)
    users.append(new_user)
    print("Registered new user", new_user)
    print(users)


register("alice", None)
register("bob", "password")
register("bob", "otherpassword")


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
        for existing_user in users:
            result = existing_user.check(username, password)
            if result == 0:
                logged_on = True
                return "Logged in successfully."
            elif result == 1:
                return "Password incorrect."
            elif result == 2:
                return "User not found."

            
    elif request.method == "GET":
        with open(folder_name + "login.html", "r") as file:
            return file.read()


@app.route("/logout")
def logout():
    global logged_on
    if logged_on:
        logged_on = False
        return "Successfully logged out."
    else:
        return "You are not logged in."



app.run(debug=True, host="0.0.0.0", port=16000)