"""Функции сохранения и загрузки объектов предметной области в JSON."""

import json
from pathlib import Path
from typing import List, Optional

from models import Parameter, Profile, Setting, User


def _read_json(filename: str) -> list:
    """Прочитать список записей из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Предупреждение: файл {filename} повреждён.")
        return []


def _write_json(filename: str, data: list) -> None:
    """Записать список записей в JSON-файл."""
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def find_user_by_id(users: List[User], user_id: int) -> Optional[User]:
    """Найти пользователя по идентификатору."""
    for user in users:
        if user.id == user_id:
            return user
    return None


def find_profile_by_id(
    profiles: List[Profile],
    profile_id: int,
) -> Optional[Profile]:
    """Найти профиль по идентификатору."""
    for profile in profiles:
        if profile.id == profile_id:
            return profile
    return None


def find_setting_by_id(
    settings: List[Setting],
    setting_id: int,
) -> Optional[Setting]:
    """Найти настройку по идентификатору."""
    for setting in settings:
        if setting.id == setting_id:
            return setting
    return None


def load_users(filename: str) -> List[User]:
    """Загрузить пользователей из JSON-файла."""
    return [User.from_data(item) for item in _read_json(filename)]


def save_users(filename: str, users: List[User]) -> None:
    """Сохранить пользователей в JSON-файл."""
    data = [
        {"id": user.id, "username": user.username, "email": user.email}
        for user in users
    ]
    _write_json(filename, data)


def load_profiles(filename: str, users: List[User]) -> List[Profile]:
    """Загрузить профили из JSON-файла, связав их с пользователями."""
    profiles = []
    for item in _read_json(filename):
        user = find_user_by_id(users, item["user_id"])
        if user is None:
            continue
        profile = Profile(item["id"], user, item["name"], item["description"])
        profiles.append(profile)
    return profiles


def save_profiles(filename: str, profiles: List[Profile]) -> None:
    """Сохранить профили в JSON-файл."""
    data = [
        {
            "id": profile.id,
            "user_id": profile.user.id,
            "name": profile.name,
            "description": profile.description,
        }
        for profile in profiles
    ]
    _write_json(filename, data)


def load_settings(filename: str, profiles: List[Profile]) -> List[Setting]:
    """Загрузить настройки из JSON-файла, связав их с профилями."""
    settings = []
    for item in _read_json(filename):
        profile = find_profile_by_id(profiles, item["profile_id"])
        if profile is None:
            continue
        setting = Setting(item["id"], profile, item["category"])
        profile.add_setting(setting)
        settings.append(setting)
    return settings


def save_settings(filename: str, settings: List[Setting]) -> None:
    """Сохранить настройки в JSON-файл."""
    data = [
        {
            "id": setting.id,
            "profile_id": setting.profile.id,
            "category": setting.category,
        }
        for setting in settings
    ]
    _write_json(filename, data)


def load_parameters(filename: str, settings: List[Setting]) -> List[Parameter]:
    """Загрузить параметры из JSON-файла, связав их с настройками."""
    parameters = []
    for item in _read_json(filename):
        setting = find_setting_by_id(settings, item["setting_id"])
        if setting is None:
            continue
        parameter = Parameter(
            item["id"],
            setting,
            item["key"],
            item["value"],
            item["value_type"],
            item["default_value"],
            item.get("min_value"),
            item.get("max_value"),
            item.get("allowed_values"),
        )
        setting.add_parameter(parameter)
        parameters.append(parameter)
    return parameters


def save_parameters(filename: str, parameters: List[Parameter]) -> None:
    """Сохранить параметры в JSON-файл."""
    data = [
        {
            "id": parameter.id,
            "setting_id": parameter.setting.id,
            "key": parameter.key,
            "value": parameter.value,
            "value_type": parameter.value_type,
            "default_value": parameter.default_value,
            "min_value": parameter.min_value,
            "max_value": parameter.max_value,
            "allowed_values": parameter.allowed_values,
        }
        for parameter in parameters
    ]
    _write_json(filename, data)
