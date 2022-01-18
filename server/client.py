import requests

url = "http://192.168.1.43:5000/login"

data = {
    "username": "bob",
    "password": "techtalents"
}

r = requests.post(url, data=data)
if r.status_code == 200:
    print(r.text)
else:
    print("Request error.", r.status_code)
