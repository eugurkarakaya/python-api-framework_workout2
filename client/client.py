import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user(user_id):
    response=requests.get(f"{BASE_URL}/users/{user_id}")
    return response

def post_data():
    payload={
        "userid":1,
        "name":"Erdem"
    }
    response=requests.post(f"{BASE_URL}/users",json=payload)
    return response


