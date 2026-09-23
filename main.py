"""Практическая работа №2.

Консольное приложение "Система настройки пользовательских профилей":
функциональная модель на коллекциях словарей.
"""

from typing import List

from parameters import (
    add_parameter,
    check_parameter_value,
    filter_parameters_by_type,
    find_parameter,
    get_parameter_status,
    reset_parameter_to_default,
    show_parameters,
    sort_parameters_by_key,
    update_parameter_value,
    validate_parameter_value,
)
from profiles import (
    add_profile,
    find_profiles_by_name,
    show_profiles,
    sort_profiles,
)
from settings import add_setting, find_settings_by_profile, show_settings
from storage import (
    load_parameters,
    load_profiles,
    load_settings,
    save_parameters,
    save_profiles,
    save_settings,
)
from utils import input_choice, input_int

PROFILES_FILE = "data/profiles.json"
SETTINGS_FILE = "data/settings.json"
PARAMETERS_FILE = "data/parameters.json"

MENU = """
=== Система настройки пользовательских профилей ===

1. Показать профили
2. Найти профиль по названию
3. Показать настройки профиля
4. Показать параметры настройки
5. Добавить профиль
6. Добавить настройку
7. Добавить параметр
8. Изменить значение параметра
9. Сбросить параметр к значению по умолчанию
10. Показать параметры по типу
11. Проверить значение параметра (без изменения)
0. Выход
"""


def create_new_parameter(parameters: List[dict]) -> None:
    """Пользовательский сценарий добавления параметра."""
    setting_id = input_int("ID настройки: ")
    key = input("Ключ параметра: ")
    value_type = input_choice(
        "Тип параметра (str/int/bool): ", ["str", "int", "bool"],
    )
    if value_type == "int":
        value = input_int("Значение: ")
        default_value = input_int("Значение по умолчанию: ")
    elif value_type == "bool":
        raw_bool = input_choice(
            "Значение (true/false): ", ["true", "false"],
        )
        value = raw_bool == "true"
        default_value = value
    else:
        value = input("Значение: ")
        default_value = value
    parameter = add_parameter(
        parameters, setting_id, key, value, value_type, default_value,
    )
    print(f"Добавлен параметр: {parameter['key']} = {parameter['value']}")


def change_parameter_value(parameters: List[dict]) -> None:
    """Пользовательский сценарий изменения значения параметра."""
    setting_id = input_int("ID настройки: ")
    key = input("Ключ параметра: ")
    parameter = find_parameter(parameters, setting_id, key)
    if parameter is None:
        print("Параметр не найден.")
        return
    if parameter["value_type"] == "int":
        new_value = input_int("Новое значение: ")
    else:
        new_value = input("Новое значение: ")
    try:
        updated = update_parameter_value(
            parameters, setting_id, key, new_value,
        )
    except KeyError as error:
        print(f"Ошибка: {error}")
        return
    is_valid = validate_parameter_value(parameter, new_value)
    print(get_parameter_status(is_valid))
    if updated:
        print("Значение сохранено.")


def preview_parameter_value(parameters: List[dict]) -> None:
    """Проверить, допустимо ли значение параметра, не изменяя его."""
    setting_id = input_int("ID настройки: ")
    key = input("Ключ параметра: ")
    parameter = find_parameter(parameters, setting_id, key)
    if parameter is None:
        print("Параметр не найден.")
        return
    if parameter["value_type"] == "int":
        candidate = input_int("Проверяемое значение: ")
    else:
        candidate = input("Проверяемое значение: ")
    is_valid = check_parameter_value(parameters, setting_id, key, candidate)
    print(get_parameter_status(is_valid))


def main() -> None:
    """Точка запуска приложения."""
    profiles = load_profiles(PROFILES_FILE)
    settings = load_settings(SETTINGS_FILE)
    parameters = load_parameters(PARAMETERS_FILE)

    while True:
        print(MENU)
        choice = input("Выберите действие: ")

        if choice == "1":
            show_profiles(sort_profiles(profiles))
        elif choice == "2":
            query = input("Подстрока названия: ")
            show_profiles(find_profiles_by_name(profiles, query))
        elif choice == "3":
            profile_id = input_int("ID профиля: ")
            show_settings(find_settings_by_profile(settings, profile_id))
        elif choice == "4":
            setting_id = input_int("ID настройки: ")
            show_parameters(
                [p for p in parameters if p["setting_id"] == setting_id],
            )
        elif choice == "5":
            name = input("Название профиля: ")
            owner = input("Владелец: ")
            description = input("Описание: ")
            add_profile(profiles, name, owner, description)
        elif choice == "6":
            profile_id = input_int("ID профиля: ")
            category = input("Категория настройки: ")
            add_setting(settings, profile_id, category)
        elif choice == "7":
            create_new_parameter(parameters)
        elif choice == "8":
            change_parameter_value(parameters)
        elif choice == "9":
            setting_id = input_int("ID настройки: ")
            key = input("Ключ параметра: ")
            if reset_parameter_to_default(parameters, setting_id, key):
                print("Параметр сброшен к значению по умолчанию.")
            else:
                print("Параметр не найден.")
        elif choice == "10":
            value_type = input_choice(
                "Тип параметра (str/int/bool): ", ["str", "int", "bool"],
            )
            matching = filter_parameters_by_type(parameters, value_type)
            show_parameters(sort_parameters_by_key(list(matching)))
        elif choice == "11":
            preview_parameter_value(parameters)
        elif choice == "0":
            save_profiles(PROFILES_FILE, profiles)
            save_settings(SETTINGS_FILE, settings)
            save_parameters(PARAMETERS_FILE, parameters)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
