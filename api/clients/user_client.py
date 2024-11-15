from .base_client import BaseClient

class UserClient(BaseClient):
    def create_user(self, user_data):
        return self.post("users", data=user_data)

    def get_user(self, user_id):
        return self.get(f"users/{user_id}")

    def delete_user(self, user_id):
        return self.delete(f"users/{user_id}")
