"""Функции сохранения и загрузки данных проекта в формате JSON."""

import json
from pathlib import Path
from typing import List


def load_data(filename: str) -> List[dict]:
    """Загрузить список записей из JSON-файла.

    Если файл отсутствует или содержит некорректный JSON,
    возвращается пустой список.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Предупреждение: файл {filename} повреждён, "
              "данные не загружены.")
        return []


def save_data(filename: str, data: List[dict]) -> None:
    """Сохранить список записей в JSON-файл."""
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_profiles(filename: str) -> List[dict]:
    """Загрузить профили из JSON-файла."""
    return load_data(filename)


def save_profiles(filename: str, profiles: List[dict]) -> None:
    """Сохранить профили в JSON-файл."""
    save_data(filename, profiles)


def load_settings(filename: str) -> List[dict]:
    """Загрузить настройки из JSON-файла."""
    return load_data(filename)


def save_settings(filename: str, settings: List[dict]) -> None:
    """Сохранить настройки в JSON-файл."""
    save_data(filename, settings)


def load_parameters(filename: str) -> List[dict]:
    """Загрузить параметры из JSON-файла."""
    return load_data(filename)


def save_parameters(filename: str, parameters: List[dict]) -> None:
    """Сохранить параметры в JSON-файл."""
    save_data(filename, parameters)
