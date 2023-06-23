from dataclasses import dataclass
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash


class User:

    def __init__(self, nickname, email):
        self.nickname = nickname
        self.email = email
        self.password_hash = None
        self.messages = set()

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def generate_email_hash(email):
        encoded = email.encode('utf-8')
        return hashlib.md5(encoded).hexdigest()

    def verify_email(self, password):
        return check_password_hash(self.password_hash, password)


@dataclass(unsafe_hash=True)
class Message:

    author: User
    body: str
