"""Практическая работа №3.

Консольное приложение "Система настройки пользовательских профилей":
объектная модель предметной области (User, Profile, Setting, Parameter).
"""

from typing import List

from models import Parameter, Profile, Setting
from storage import (
    find_profile_by_id,
    find_setting_by_id,
    load_parameters,
    load_profiles,
    load_settings,
    load_users,
    save_parameters,
    save_profiles,
    save_settings,
    save_users,
)
from utils import input_choice, input_int, log_call

USERS_FILE = "data/users.json"
PROFILES_FILE = "data/profiles.json"
SETTINGS_FILE = "data/settings.json"
PARAMETERS_FILE = "data/parameters.json"

MENU = """
=== Система настройки пользовательских профилей ===

1. Показать профили
2. Показать настройки профиля
3. Показать параметры настройки
4. Добавить настройку
5. Добавить параметр
6. Изменить значение параметра
7. Сбросить параметр к значению по умолчанию
0. Выход
"""


def show_profiles(profiles: List[Profile]) -> None:
    """Вывести список профилей."""
    if not profiles:
        print("Профили не найдены.")
        return
    for profile in profiles:
        print(f"[{profile.id}] {profile}")


def show_settings(settings: List[Setting]) -> None:
    """Вывести список настроек."""
    if not settings:
        print("Настройки не найдены.")
        return
    for setting in settings:
        print(f"[{setting.id}] {setting}")


def show_parameters(parameters: List[Parameter]) -> None:
    """Вывести список параметров."""
    if not parameters:
        print("Параметры не найдены.")
        return
    for parameter in parameters:
        print(f"[{parameter.id}] {parameter}")


@log_call
def create_new_setting(
    profiles: List[Profile],
    settings: List[Setting],
) -> None:
    """Пользовательский сценарий добавления настройки в профиль."""
    profile_id = input_int("ID профиля: ")
    profile = find_profile_by_id(profiles, profile_id)
    if profile is None:
        print("Профиль не найден.")
        return
    category = input("Категория настройки: ")
    new_id = len(settings) + 1
    setting = Setting(new_id, profile, category)
    profile.add_setting(setting)
    settings.append(setting)
    print(f"Добавлена настройка: {setting}")


def create_new_parameter(
    settings: List[Setting],
    parameters: List[Parameter],
) -> None:
    """Пользовательский сценарий добавления параметра в настройку."""
    setting_id = input_int("ID настройки: ")
    setting = find_setting_by_id(settings, setting_id)
    if setting is None:
        print("Настройка не найдена.")
        return
    key = input("Ключ параметра: ")
    value_type = input_choice(
        "Тип параметра (str/int/bool): ", ["str", "int", "bool"],
    )
    if value_type == "int":
        value = input_int("Значение: ")
        default_value = input_int("Значение по умолчанию: ")
    elif value_type == "bool":
        raw_bool = input_choice("Значение (true/false): ", ["true", "false"])
        value = raw_bool == "true"
        default_value = value
    else:
        value = input("Значение: ")
        default_value = value
    new_id = len(parameters) + 1
    parameter = Parameter(
        new_id, setting, key, value, value_type, default_value,
    )
    setting.add_parameter(parameter)
    parameters.append(parameter)
    print(f"Добавлен параметр: {parameter}")


def change_parameter_value(parameters: List[Parameter]) -> None:
    """Пользовательский сценарий изменения значения параметра."""
    parameter_id = input_int("ID параметра: ")
    parameter = next((p for p in parameters if p.id == parameter_id), None)
    if parameter is None:
        print("Параметр не найден.")
        return
    if parameter.value_type == "int":
        new_value = input_int("Новое значение: ")
    else:
        new_value = input("Новое значение: ")
    if parameter.update_value(new_value):
        print("Значение сохранено.")
    else:
        print("Недопустимое значение параметра.")


@log_call
def reset_parameter(parameters: List[Parameter]) -> None:
    """Пользовательский сценарий сброса параметра к значению по умолчанию."""
    parameter_id = input_int("ID параметра: ")
    parameter = next((p for p in parameters if p.id == parameter_id), None)
    if parameter is None:
        print("Параметр не найден.")
        return
    parameter.reset_to_default()
    print(f"Параметр сброшен: {parameter}")


def main() -> None:
    """Точка запуска приложения."""
    users = load_users(USERS_FILE)
    profiles = load_profiles(PROFILES_FILE, users)
    settings = load_settings(SETTINGS_FILE, profiles)
    parameters = load_parameters(PARAMETERS_FILE, settings)

    while True:
        print(MENU)
        choice = input("Выберите действие: ")

        if choice == "1":
            show_profiles(profiles)
        elif choice == "2":
            profile_id = input_int("ID профиля: ")
            profile = find_profile_by_id(profiles, profile_id)
            if profile is None:
                print("Профиль не найден.")
            else:
                show_settings(profile.settings)
        elif choice == "3":
            setting_id = input_int("ID настройки: ")
            setting = find_setting_by_id(settings, setting_id)
            if setting is None:
                print("Настройка не найдена.")
            else:
                show_parameters(setting.parameters)
        elif choice == "4":
            create_new_setting(profiles, settings)
        elif choice == "5":
            create_new_parameter(settings, parameters)
        elif choice == "6":
            change_parameter_value(parameters)
        elif choice == "7":
            reset_parameter(parameters)
        elif choice == "0":
            save_users(USERS_FILE, users)
            save_profiles(PROFILES_FILE, profiles)
            save_settings(SETTINGS_FILE, settings)
            save_parameters(PARAMETERS_FILE, parameters)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
