from flask import Flask, render_template
from model import User, Message

app = Flask(__name__)


def create_sample_dbs():
    bob = User(email='bob@example.com')
    message1 = bob.create_message('I like pancakes!')
    message2 = bob.create_message('I like chocolates!')

    alice = User(email='alice@example.com')
    message3 = alice.create_message('I wanna break free')
    message4 = alice.create_message('To be a rock and not to roll')

    return {bob, alice}, {message1, message2, message3, message4}


user_db, message_db = create_sample_dbs()


@app.route('/')
def home():
    messages = list(message_db)
    user_count = len(user_db)
    return render_template('home.html', messages=messages, user_count=user_count)


if __name__ == '__main__':
    app.run()