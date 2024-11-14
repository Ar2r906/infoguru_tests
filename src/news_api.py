import requests

class ApiNews:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_news(self, endpoint):
        return requests.get(f"{self.base_url}/{endpoint}")

    def get_news_id(self, endpoint, news_id):
        return requests.get(f"{self.base_url}/{endpoint}/{news_id}")

    def create_news(self, endpoint, data):
        return requests.post(f"{self.base_url}/{endpoint}", json=data)

    def put_news(self, endpoint, news_id, data):
        return requests.put(f"{self.base_url}/{endpoint}/{news_id}", json=data)

    def delete_news(self, endpoint, news_id):
        return requests.delete(f"{self.base_url}/{endpoint}/{news_id}")