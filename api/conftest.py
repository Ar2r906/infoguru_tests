import pytest
from api.clients.user_client import UserClient

@pytest.fixture
def user_client():
    return UserClient()