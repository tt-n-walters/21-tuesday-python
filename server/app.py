from flask import Flask, request
import os
import hashlib
import time
import json
import datetime


from users import *
import encryption


folder_name = os.path.dirname(os.path.abspath(__file__)) + "/"
app = Flask(__name__)


logged_on = False


messages = []


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
    strings = []
    for message in messages:
        name, text, time = message.values()
        decrypted = encryption.decrypt(text)
        date = datetime.datetime.fromtimestamp(time).strftime("%c")
        string = "{} <b>{}</b> :: {}".format(date, name, decrypted)
        strings.append(string)

    return "<br><br>".join(strings)


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

        cipher = encryption.encrypt(text)
        
        message = {
            "username": name,
            "text": cipher,
            "time_sent": time_sent
        }
        messages.append(message)
        save_messages()
        return "Message sent successfully."



load_users_from_disk()
read_messages()
# register("dominic", "helloworld")
app.run(debug=True, host="0.0.0.0", port=16000)
