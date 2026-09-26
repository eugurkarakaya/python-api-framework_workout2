from unittest.mock import patch
from client.client import get_user,post_data
from test.conftest import mocking_get_response
import pytest

@pytest.mark.parametrize("user_id,expected_id",[(1,1),(2,2),(3,3),(4,4),(5,5)])
def test_get_user(user_id,expected_id,mocking_get_response):
    with patch("client.client.requests.get", return_value=mocking_get_response) as mock_get:
        response=get_user(user_id)
        assert response.status_code == 200
        assert response.json()["id"] == expected_id
        assert response.json()["name"] == "Erdem"

        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/{user_id}")

def test_post_data(mocking_post_response):
    with patch("client.client.requests.post",return_value=mocking_post_response)as mock_post:

        response=post_data()

        assert response.status_code == 201
        assert response.json()["id"] == 1
        assert response.json()["name"] == "Erdem"

        mock_post.assert_called_once_with(
            "https://jsonplaceholder.typicode.com/users",
            json={"id":1,
                  "name":"Erdem"},
       )
