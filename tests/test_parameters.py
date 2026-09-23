"""Тесты класса Parameter."""

from models import Parameter, Profile, Setting, User


def _make_setting() -> Setting:
    user = User(1, "Иван Петров", "ivan@example.com")
    profile = Profile(1, user, "Рабочий профиль", "Описание")
    return Setting(1, profile, "Внешний вид")


def test_parameter_creation():
    setting = _make_setting()
    parameter = Parameter(
        1, setting, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert parameter.value == 14
    assert parameter.setting is setting


def test_parameter_is_valid_value():
    setting = _make_setting()
    parameter = Parameter(
        1, setting, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert parameter.is_valid_value(20)
    assert not parameter.is_valid_value(40)
    assert not parameter.is_valid_value("14")


def test_parameter_update_value():
    setting = _make_setting()
    parameter = Parameter(
        1, setting, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert parameter.update_value(18)
    assert parameter.value == 18
    assert not parameter.update_value(100)
    assert parameter.value == 18


def test_parameter_reset_to_default():
    setting = _make_setting()
    parameter = Parameter(
        1, setting, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    parameter.update_value(18)
    parameter.reset_to_default()
    assert parameter.value == 12


def test_parameter_validate_type_staticmethod():
    assert Parameter.validate_type(14, "int")
    assert not Parameter.validate_type("14", "int")
    assert Parameter.validate_type(True, "bool")
