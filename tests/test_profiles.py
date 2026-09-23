"""Тесты функций работы с профилями."""

from profiles import add_profile, find_profiles_by_name, sort_profiles


def test_add_profile():
    profiles = []
    profile = add_profile(profiles, "Рабочий профиль", "Иван", "Описание")
    assert len(profiles) == 1
    assert profile["name"] == "Рабочий профиль"


def test_find_profiles_by_name():
    profiles = []
    add_profile(profiles, "Рабочий профиль", "Иван", "Описание")
    add_profile(profiles, "Личный профиль", "Иван", "Описание")
    found = find_profiles_by_name(profiles, "рабочий")
    assert len(found) == 1
    assert found[0]["name"] == "Рабочий профиль"


def test_sort_profiles():
    profiles = []
    add_profile(profiles, "Личный профиль", "Иван", "Описание")
    add_profile(profiles, "Рабочий профиль", "Иван", "Описание")
    sorted_profiles = sort_profiles(profiles)
    assert sorted_profiles[0]["name"] == "Личный профиль"
