import string
from random import random

import pytest
import allure
import os

import requests
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

# def generate_password(length):
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#     digits = string.digits
#     symbols = string.punctuation
#
#     password = [
#         random.choice(lower),
#         random.choice(upper),
#         random.choice(digits),
#         random.choice(symbols),
#     ]
#
#     all_characters = lower + upper + digits + symbols
#     password += random.choices(all_characters, k=length)
#
#     random.shuffle(password)
#     print(password)
#     return ''.join(password)

@allure.title('Регистрация, негативное тестирование')
@allure.description('Ответ 413')
@pytest.mark.api
def test_register_none_patr():
    reg_value = [{
        "second_name": "Ibragimov_Test",
        "first_name": "Artur_Test",
        "patr_name": "",
        "email": "artur_ibragimov_1809@mail.ru",
        "password": "12345&*()_gTYG"
    }]
    login_url = f"{BASE_URL}/api/auths/signin"
    response = requests.post(login_url, json=reg_value)
    assert response.status_code == 413

# def tets_register_none_fname():
