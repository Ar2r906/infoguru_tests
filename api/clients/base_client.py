import requests
from common.config import BASE_URL, HEADERS

class BaseClient:
    def __init__(self,  base_url = BASE_URL, headers = HEADERS):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params, headers=self.headers)
        response.raise_for_status()
        return response

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self.headers)
        response.raise_for_status()
        return response

    def delete(self, endpoint, params=None):
        response = requests.delete(f"{self.base_url}/{endpoint}", params=params, headers=self.headers)
        response.raise_for_status()
        return response
    