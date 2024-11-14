from src.api_client import ApiClient

class ClientAPI(ApiClient):
    def get_clients(self):
        return self.get_users("/users")

    def get_clients_id(self, client_id):
        return self.get_user_id(f"/users/{client_id}")

    def create_client(self, data):
        return self.create_user("/register", data)

    def delete_client(self, client_id):
        return self.delete_user(f"/users/{client_id}")