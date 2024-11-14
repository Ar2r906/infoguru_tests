import requests
import pytest
import allure
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TEST_USER_EMAIL = os.getenv("TEST_USER.EMAIL")
TEST_USER_PASSWORD = os.getenv("TEST_USER.PASSWORD")

@allure.title("Позитивное тестирование авторизации в системе")
@allure.description("Используются корректные логин и пароль, на выходе должен быть статус 200")
@pytest.mark.api
def test_login_positive():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 200, "login failed"
    assert "accessToken" in response.json(), "No accessToken in response"

    token = response.json()["accessToken"]
    uid = response.json()["uid"]
    refreshToken = response.json()["refreshToken"]
    # email = response.json()["Email"]
    # name = response.json()["Name"]

    headers = {"Authorization": f"Data {token, uid, refreshToken}"}
    user_info_url = f"{BASE_URL}/api/news"
    user_info_response = requests.get(user_info_url, headers=headers)

    assert user_info_response.status_code == 200, "Failed to open news page"

@allure.title("Негативное тестирование без ввода пароля")
@allure.description("Используются корректный логин но без пароля, на выходе должен быть статус 413")
@pytest.mark.api
def test_login_none_pass():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": "1234567",
        "password": ""
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 413, "login failed"

@allure.title("Негативное тестирование без ввода логина")
@allure.description("Используются корректный пароль но без логина, на выходе должен быть статус 413")
@pytest.mark.api
def test_login_none_email():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": "",
        "password": "12345678"
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 413, "login failed"

@allure.title("Негативное тестирование без ввода пароля")
@allure.description("Используются корректный логин но без пароля, на выходе должен быть статус 413")
@pytest.mark.api
def test_login_none_data():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": "",
        "password": ""
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 413, "login failed"

@allure.title("Негативное тестирование с использованием некорректного пароля")
@allure.description("Используется корректная почта, но некорректный пароль, на выходе статус 414")
@pytest.mark.api
def test_login_not_valid_pass():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": TEST_USER_EMAIL,
        "password": "12345678"
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 414, "login failed"

@allure.title("Негативное тестирование с использованием некорректного логин")
@allure.description("Используется корректный пароль, но некорректный логин, на выходе статус 404")
@pytest.mark.api
def test_login_not_valid_email():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": "12345678",
        "password": TEST_USER_PASSWORD
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 404, "login failed"

@allure.title("Негативное тестирование с использованием некорректных логина и пароля")
@allure.description("Используется некорректный пароль и некорректный логин, на выходе статус 404")
@pytest.mark.api
def test_login_not_valid_data():
    login_url = f"{BASE_URL}/api/auths/signin"
    payload = {
        "email": "12345678",
        "password": "12345678"
    }

    response = requests.post(login_url, json=payload)
    assert response.status_code == 404, "login failed"