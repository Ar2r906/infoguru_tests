import os

import pytest
import requests
from playwright.sync_api import sync_playwright
from src.api_client import ApiClient
from dotenv import load_dotenv
load_dotenv()

# @pytest.fixture
# def api_client():
#     session = requests.Session()
#     session.headers.update({
#         'Authorization': 'Bearer your_token_here'
#     })
#     return session
base_url = os.getenv("BASE_URL")

@pytest.fixture
def api_client():
    return ApiClient(base_url)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()