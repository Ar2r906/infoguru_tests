import pytest

@pytest.mark.parametrize("user_data", [
    {"name": "NAME", "email": "EMAIL", "password": "PASSWORD"},
    {"name": "NAME", "email": "EMAIL", "password": "SECUREPASSWORD"},
])
def test_registration_user(user_client, user_data):
    # Create user
    response = user_client.create_user(user_data)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["name"] == user_data["name"]
    assert created_user["email"] == user_data["email"]

    # Check that user is created
    user_id = created_user["id"]
    response = user_client.get_user(user_id)
    assert response.status_code == 200
    fetched_user = response.json()
    assert fetched_user["id"] == user_id

    # Delete user
    response = user_client.delete_user(user_id)
    assert response.status_code == 204