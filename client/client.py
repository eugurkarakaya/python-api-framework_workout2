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

    headers={
        "Content-Type":"application/json"
    }

    response=requests.post(f"{BASE_URL}/users",json=payload,headers=headers)
    return response


