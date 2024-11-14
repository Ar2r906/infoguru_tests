import requests

class ApiAnswers:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_answers(self, endpoint):
        return requests.get(f"{self.base_url}/{endpoint}")

    def create_answers(self, endpoint, data):
        return requests.post(f"{self.base_url}/{endpoint}", json=data)

    def delete_answers(self, endpoint):
        return requests.delete(f"{self.base_url}/{endpoint}")

    def put_answers(self, endpoint, data):
        return requests.put(f"{self.base_url}/{endpoint}", json=data)