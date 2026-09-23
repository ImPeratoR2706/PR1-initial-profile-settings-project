"""Тесты функций работы с настройками."""

from settings import (
    add_setting,
    find_setting_by_category,
    find_settings_by_profile,
)


def test_add_setting():
    settings = []
    setting = add_setting(settings, 1, "Внешний вид")
    assert len(settings) == 1
    assert setting["category"] == "Внешний вид"


def test_find_settings_by_profile():
    settings = []
    add_setting(settings, 1, "Внешний вид")
    add_setting(settings, 2, "Уведомления")
    found = find_settings_by_profile(settings, 1)
    assert len(found) == 1
    assert found[0]["category"] == "Внешний вид"


def test_find_setting_by_category():
    settings = []
    add_setting(settings, 1, "Внешний вид")
    setting = find_setting_by_category(settings, 1, "Внешний вид")
    assert setting is not None
    assert setting["profile_id"] == 1
