import random
import allure
import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

base_url = os.getenv("BASE_URL")

@pytest.fixture(scope='session')
def api_request_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        api_context = context.request
        yield api_context
        browser.close()

@allure.title('Новости get')
@allure.description('Запрос на получение новостей, ответ 200')
@pytest.mark.api
def test_get_allNews(api_request_context):
    response = api_request_context.get(f"{base_url}api/news/")
    assert response.status == 200
    data = response.json()

    assert len(data) > 0

    expected_keys = {"id", "title", "content", "image", "createdAt", "updatedAt"}
    first_item = data[0]
    assert isinstance(first_item, dict), 'Ожидаслся словарь в элементе списка'
    assert expected_keys.issubset(first_item.keys()), 'Отсутсвуют необходимые ключи в ответе'

@allure.title('Новости get по id')
@allure.description('Запрос на получение новости по ее id, ответ 200')
@pytest.mark.api
def test_get_idNews(api_request_context):
    response = api_request_context.get(f"{base_url}api/news/31")
    assert response.status == 200
    data = response.json()
    assert len(data) > 0

    assert int(data["id"]) == 31
    assert data["title"] == "Двухфакторная аутентификация, что такое и для чего она нужна."

@allure.title('Новости get по id (негативный)')
@allure.description('Запрос на получение новости по ее id, ответ 200')
@pytest.mark.api
def test_get_idNews_negative(api_request_context):
    random_value = random.randint(-1000, 1000)
    response = api_request_context.get(f"{base_url}api/news/{random_value}")

    if response.status != 404:
        data = response.json()
        assert response.status == 200
        print(data["id"])
    else:
        assert response.status == 404
