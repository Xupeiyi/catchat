from catchat.model import User, Message


def test_mapper(session):
    bob = User(email='bob@example.com')
    _ = bob.create_message("I love ice-cream!")
    _ = bob.create_message("I love pineapple!")

    session.add(bob)
    session.commit()

    messages = session.query(Message).all()
    m0 = messages[0]
    m1 = messages[1]
    assert m0.author is bob and m1.author is bob
    assert {m0.body, m1.body} == {'I love ice-cream!', 'I love pineapple!'}
