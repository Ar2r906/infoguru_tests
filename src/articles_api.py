import requests

class ApiArticles:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_articles(self, endpoint):
        return requests.get(f"{self.base_url}/{endpoint}")

    def create_articles(self, endpoint, data):
        return requests.post(f"{self.base_url}/{endpoint}", json=data)

    def delete_articles(self, endpoint):
        return requests.delete(f"{self.base_url}/{endpoint}")

    def put_articles(self, endpoint, data):
        return requests.put(f"{self.base_url}/{endpoint}", json=data)