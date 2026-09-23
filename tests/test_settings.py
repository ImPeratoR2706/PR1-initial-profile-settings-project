"""Тесты класса Setting."""

from models import Parameter, Profile, Setting, User


def _make_setting() -> Setting:
    user = User(1, "Иван Петров", "ivan@example.com")
    profile = Profile(1, user, "Рабочий профиль", "Описание")
    return Setting(1, profile, "Внешний вид")


def test_setting_creation():
    setting = _make_setting()
    assert setting.id == 1
    assert setting.category == "Внешний вид"
    assert setting.parameters == []


def test_setting_add_and_find_parameter():
    setting = _make_setting()
    parameter = Parameter(1, setting, "theme", "dark", "str", "light")
    setting.add_parameter(parameter)
    assert setting.find_parameter("theme") is parameter
    assert setting.find_parameter("font_size") is None


def test_setting_str():
    setting = _make_setting()
    assert "Внешний вид" in str(setting)
