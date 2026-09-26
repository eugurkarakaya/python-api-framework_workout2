from unittest.mock import patch,Mock
import pytest


@pytest.fixture
def mocking_get_response(user_id): #her user_id için mock yap. parametrize'den ötürü
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": user_id, "name": "Erdem"}
    return mock_response

@pytest.fixture
def mocking_post_response():
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": 1, "name": "Erdem"}
    return mock_response