import os
import hashlib


folder_name = os.path.dirname(os.path.abspath(__file__)) + "/"

users = []

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
