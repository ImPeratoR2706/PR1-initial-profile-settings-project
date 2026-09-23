"""Тесты класса Profile."""

from models import Profile, Setting, User


def _make_user() -> User:
    return User(1, "Иван Петров", "ivan@example.com")


def test_profile_creation():
    user = _make_user()
    profile = Profile(1, user, "Рабочий профиль", "Описание")
    assert profile.id == 1
    assert profile.user is user
    assert profile.settings == []


def test_profile_add_and_find_setting():
    user = _make_user()
    profile = Profile(1, user, "Рабочий профиль", "Описание")
    setting = Setting(1, profile, "Внешний вид")
    profile.add_setting(setting)
    assert profile.find_setting("Внешний вид") is setting
    assert profile.find_setting("Уведомления") is None


def test_profile_str():
    user = _make_user()
    profile = Profile(1, user, "Рабочий профиль", "Описание")
    assert "Рабочий профиль" in str(profile)
    assert "Иван Петров" in str(profile)
