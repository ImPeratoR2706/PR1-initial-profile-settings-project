"""Практическая работа №1.

Стартовый сценарий индивидуального проекта
"Система настройки пользовательских профилей".

Сценарий проверяет, попадает ли значение числового параметра
настройки в допустимый диапазон, и выводит информацию о нём.
"""

from datetime import date

profile_name = "Рабочий профиль"
setting_category = "Внешний вид"
parameter_key = "font_size"
parameter_value = 14
min_value = 10
max_value = 24
updated_at = date(2026, 9, 17)


def is_value_in_range(value: int, min_value: int, max_value: int) -> bool:
    """Проверить, находится ли значение параметра в допустимом диапазоне."""
    return min_value <= value <= max_value


def get_parameter_status(is_valid: bool) -> str:
    """Вернуть текстовый статус параметра."""
    if is_valid:
        return "Значение параметра допустимо"
    return "Недопустимое значение параметра"


def format_parameter_info(
    profile: str,
    category: str,
    key: str,
    value: int,
) -> str:
    """Сформировать строку с описанием параметра профиля."""
    return f"Профиль «{profile}» -> {category} -> {key} = {value}"


is_valid = is_value_in_range(parameter_value, min_value, max_value)

print(format_parameter_info(
    profile_name, setting_category, parameter_key, parameter_value,
))
print(f"Допустимый диапазон: от {min_value} до {max_value}")
print(f"Дата обновления: {updated_at}")
print(get_parameter_status(is_valid))
