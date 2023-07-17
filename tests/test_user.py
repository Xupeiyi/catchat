import unittest
from catchat.model import User


class CreateMessageTest(unittest.TestCase):
    def test_can_retrieve_created_messages(self):
        bob = User(email='bob@example.com')
        message1 = bob.create_message('I love pancakes!')
        self.assertSetEqual(bob.messages, {message1})

    def test_messages_has_correct_creator(self):
        bob = User(email='bob@example.com')
        message1 = bob.create_message('I love pancakes!')
        self.assertEqual(bob, message1.author)


class DeleteMessageTest(unittest.TestCase):

    def test_can_delete_ones_own_words(self):
        bob = User(email='bob@example.com')
        message1 = bob.create_message('I love pancakes!')
        message2 = bob.create_message('I love ice-creams!')
        bob.delete_message(message1)
        self.assertSetEqual(bob.messages, {message2})

    def test_cannot_delete_others_words(self):
        bob = User(email='bob@example.com')
        alice = User(email='alice@example.com')
        message1 = bob.create_message('I love pancakes!')
        self.assertRaises(ValueError, alice.delete_message, message1)
