import requests

class ApiSomething:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_something(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()

    def get_something_id(self, endpoint, something_id):
        response = requests.get(f"{self.base_url}/{endpoint}/{something_id}")
        return response.json()

    def post_something(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        return response.json()

    def put_something(self, endpoint, something_id, data):
        response = requests.put(f"{self.base_url}/{endpoint}/{something_id}", json=data)
        return response.json()

    def delete_something(self, endpoint, something_id):
        response = requests.delete(f"{self.base_url}/{endpoint}/{something_id}")
        return response.json()