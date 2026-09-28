from client.client import get_user
import pytest
from unittest.mock import MagicMock,Mock,patch

@pytest.mark.parametrize("user_id,expected_id",[(1,1),(2,2),(3,3),(5,5)])
def test_get_user(user_id,expected_id):
    with patch("client.client.requests.get")as mock_get:
        mock_response=Mock()
        mock_response.status_code=200
        mock_response.json.return_value={"id":expected_id,"name":"erdemk"}
        mock_get.return_value=mock_response

        get_user(user_id)

        mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/{user_id}")

        assert mock_response.status_code == 200
        assert mock_response.json().get("id") == expected_id

