import requests

class ApiTests:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_tests(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response

    def get_test_id(self, endpoint, test_id):
        response = requests.get(f"{self.base_url}/{endpoint}/{test_id}")
        return response

    def create_tests(self, endpoint, data):
        return requests.post(f"{self.base_url}/{endpoint}", json=data)

    def delete_tests(self, endpoint, test_id):
        return requests.delete(f"{self.base_url}/{endpoint}/{test_id}")

    def put_tests(self, endpoint, test_id, data):
        return requests.put(f"{self.base_url}/{endpoint}/{test_id}", json=data)