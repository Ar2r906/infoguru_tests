import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self):
        response = requests.get(f"{self.base_url}/users")
        return response

    def get_user_id(self, client_id):
        response = requests.get(f"{self.base_url}/users/{client_id}")
        return response

    def create_user(self, data):
        response = requests.post(f"{self.base_url}/users", json=data)
        return response

    def delete_user(self, client_id):
        response = requests.delete(f"{self.base_url}/users/{client_id}")
        return response
