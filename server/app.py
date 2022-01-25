from flask import Flask, request
import os
import hashlib
import time
import json


#     deterministic
#     chaotic


folder_name = os.path.dirname(os.path.abspath(__file__)) + "/"
app = Flask(__name__)


logged_on = False


class User:
    def __init__(self, name, password):
        self.name = name
        self.hashed_password = password

    @classmethod
    def register(cls, name, password):
        encrypted = cls.hash_password(password)
        return cls(name, encrypted)
    
    @classmethod
    def hash_password(cls, password):
        hashed = hashlib.md5(password.encode("utf-8"))
        return hashed.hexdigest()
    
    def __repr__(self):
        return repr("User with name: " + repr(self.name))
    
    def check_name(self, name):
        if name == self.name:
            return True
        else:
            return False

    def check_password(self, password):
        if self.hash_password(password) == self.hashed_password:
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
messages = []

def register(name, password):
    for existing_user in users:
        print("Checking", existing_user)
        if existing_user.check_name(name):
            print("User with name", name, "already exists.")
            return

    new_user = User(name, password)
    users.append(new_user)
    print("Registered new user", new_user)
    save_users_to_disk()




def load_users_from_disk():
    with open(folder_name + "users.dat", "r") as file:
        for user_string in file.read().splitlines():
            name, password = user_string.split(":::")
            user = User(name, password)
            users.append(user)


def save_users_to_disk():
    with open(folder_name + "users.dat", "w") as file:
        for user in users:
            user_string = "{}:::{}\n".format(user.name, user.password)
            file.write(user_string)


def save_messages():
    with open(folder_name + "messages.json", "w") as file:
        file.write(json.dumps(messages))

def read_messages():
    try:
        with open(folder_name + "messages.json", "r") as file:
            data = json.loads(file.read())
            messages.extend(data)
    except:
        pass


@app.route("/")
def get_index():
    return str(messages)


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
        else:
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


@app.route("/messages", methods=["GET", "POST"])
def message():
    if request.method == "GET":
        with open(folder_name + "send_message.html", "r") as file:
            return file.read()

    elif request.method == "POST":
        name = request.form.get("username")
        text = request.form.get("text")
        time_sent = time.time()
        message = {
            "username": name,
            "text": text,
            "time_sent": time_sent
        }
        messages.append(message)
        save_messages()
        return "Message sent successfully."



load_users_from_disk()
read_messages()
# register("dominic", "helloworld")
app.run(debug=True, host="0.0.0.0", port=16000)
