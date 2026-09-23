"""Тесты класса User."""

from models import User


def test_user_creation():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert user.id == 1
    assert user.username == "Иван Петров"
    assert user.email == "ivan@example.com"


def test_user_str():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert str(user) == "Иван Петров (ivan@example.com)"


def test_user_from_data():
    data = {"id": 1, "username": "Иван Петров", "email": "ivan@example.com"}
    user = User.from_data(data)
    assert user.id == 1
    assert user.username == "Иван Петров"
