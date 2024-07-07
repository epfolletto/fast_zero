from sqlalchemy import select

from fast_zero.models import User


def teste_create_user(session):
    user = User(username='teste', email='teste@gmail.com', password='teste')
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'teste@gmail.com')
    )

    assert result.username == 'teste'
