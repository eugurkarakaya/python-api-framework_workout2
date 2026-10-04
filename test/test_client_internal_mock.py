from client.client import get_user,post_data
import pytest
from unittest.mock import MagicMock,Mock,patch

@pytest.mark.parametrize("user_id,expected_id",[(1,1),(2,2),(3,3),(4,4)])
def test_get_user(user_id,expected_id):
    with patch("client.client.requests.get")as mock_get:
        mock_response=Mock()
        mock_response.status_code=200
        mock_response.json.return_value={"id":expected_id,"name":"erdemk"}
        mock_get.return_value=mock_response

        response=get_user(user_id)

        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/{user_id}")

        assert response.status_code == 200
        assert response.json().get("id") == expected_id
        assert response.json()["name"]=="erdemk"

def test_post_data():
    with patch("client.client.requests.post")as mock_post:
        mock_response=Mock()
        mock_response.status_code=201
        mock_response.json.return_value={"userid":1,"name":"erdemk"}
        mock_post.return_value=mock_response

        mock_response=post_data()

        assert mock_response.status_code == 201
        assert mock_response.json().get("userid") == 1

        mock_post.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users",json={"userid":1,"name":"Erdem"},headers={"Content-Type": "application/json"})


def test_edge_case_user_id():
    with patch("client.client.requests.get")as mock_get:
        mock_response=Mock()
        mock_response.status_code=404
        mock_get.return_value=mock_response

        response=get_user(-1)
        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/-1")
        assert response.status_code == 404

def test_negative_test_case_not_found_404():
    with patch("client.client.requests.get")as mock_get:
        mock_response=Mock()
        mock_response.status_code=404
        mock_get.return_value=mock_response


        response=get_user(9999)

        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/9999")
        assert response.status_code == 404

def test_negative_test_case_internal_Service_Error_505():
    with patch("client.client.requests.get")as mock_get:
        mock_response=Mock()
        mock_response.status_code=505
        mock_get.return_value=mock_response

        response=get_user(1)
        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/1")
        assert response.status_code == 505