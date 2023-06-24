from dataclasses import dataclass
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash


class User:

    def __init__(self, email):
        # self.nickname = nickname
        self.email = email
        # self.password_hash = None
        self.messages = set()

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.email == self.email

    # @property
    # def password(self):
    #     raise AttributeError("password is not a readable attribute")
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # @staticmethod
    # def generate_email_hash(email):
    #     encoded = email.encode('utf-8')
    #     return hashlib.md5(encoded).hexdigest()

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def create_message(self, words):
        message = Message(author=self, body=words)
        self.messages.add(message)
        return message

    def delete_message(self, message):
        if message.author == self:
            self.messages.remove(message)
        else:
            raise ValueError("Can't delete a message of another user!")


@dataclass(unsafe_hash=True)
class Message:

    author: User
    body: str

