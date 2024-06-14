import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class UserAuth:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return "User already exists."
        self.users[username] = User(username, password)
        return "User added successfully."

    def login(self, username, password):
        user = self.users.get(username)
        if not user:
            return "User not found."
        if user.password_hash == User.hash_password(password):
            return "Login successful."
        return "Incorrect password."
