"""Функции для работы с настройками профилей."""

from typing import List, Optional


def add_setting(settings: List[dict], profile_id: int, category: str) -> dict:
    """Добавить настройку в коллекцию и вернуть созданную запись."""
    new_id = len(settings) + 1
    setting = {
        "id": new_id,
        "profile_id": profile_id,
        "category": category,
    }
    settings.append(setting)
    return setting


def find_settings_by_profile(
    settings: List[dict],
    profile_id: int,
) -> List[dict]:
    """Найти все настройки указанного профиля."""
    return [s for s in settings if s["profile_id"] == profile_id]


def find_setting_by_category(
    settings: List[dict],
    profile_id: int,
    category: str,
) -> Optional[dict]:
    """Найти настройку профиля по категории."""
    for setting in settings:
        same_profile = setting["profile_id"] == profile_id
        same_category = setting["category"] == category
        if same_profile and same_category:
            return setting
    return None


def show_settings(settings: List[dict]) -> None:
    """Вывести список настроек."""
    if not settings:
        print("Настройки не найдены.")
        return
    for setting in settings:
        print(
            f"[{setting['id']}] {setting['category']} "
            f"(профиль {setting['profile_id']})"
        )
