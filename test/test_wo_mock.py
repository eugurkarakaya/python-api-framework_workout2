from client.client import get_user,post_data
import pytest

def test_get_user():
    response=get_user(1)
    assert response.status_code == 200
    assert response.json()["name"] =="Leanne Graham"
    assert response.json()["id"]==1
    assert response.json()["username"]=="Bret"
    assert response.json()["email"]=="Sincere@april.biz"

def test_get_user_notfound():
    response=get_user(999999)
    assert response.status_code == 404

def test_post_data():
    response=post_data()
    assert response.status_code ==201
    assert response.json()["name"] == "Erdem"
    assert response.json()["userid"] == 1

    created_id=response.json()["id"]
    assert created_id is not None
    assert isinstance(created_id,int) #created_id integer mı, değil mi ?
    assert created_id >0
"""
#kod doğru, aldığın 404 hatası da tam olarak JSONPlaceholder'ın davranışından kaynaklanıyor.
def test_request_chaining_post_get():
    post_response=post_data()
    assert post_response.status_code == 201
    created_id=post_response.json()["id"]

    get_response=get_user(created_id)
    assert get_response.status_code == 200

    assert get_response.json()["name"] == "Erdem"
    assert get_response.json()["id"]==created_id
"""