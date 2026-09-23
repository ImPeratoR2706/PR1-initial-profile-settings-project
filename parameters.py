"""Функции для работы с параметрами настроек."""

from typing import Iterator, List, Optional, Union

ParameterValue = Union[str, int, bool]


def add_parameter(
    parameters: List[dict],
    setting_id: int,
    key: str,
    value: ParameterValue,
    value_type: str,
    default_value: ParameterValue,
    min_value: Optional[int] = None,
    max_value: Optional[int] = None,
    allowed_values: Optional[list] = None,
) -> dict:
    """Добавить параметр в коллекцию и вернуть созданную запись."""
    new_id = len(parameters) + 1
    parameter = {
        "id": new_id,
        "setting_id": setting_id,
        "key": key,
        "value": value,
        "value_type": value_type,
        "default_value": default_value,
        "min_value": min_value,
        "max_value": max_value,
        "allowed_values": allowed_values,
    }
    parameters.append(parameter)
    return parameter


def find_parameter(
    parameters: List[dict],
    setting_id: int,
    key: str,
) -> Optional[dict]:
    """Найти параметр настройки по ключу."""
    for parameter in parameters:
        if parameter["setting_id"] == setting_id and parameter["key"] == key:
            return parameter
    return None


def check_parameter_value(
    parameters: List[dict],
    setting_id: int,
    key: str,
    value: ParameterValue,
) -> bool:
    """Найти параметр по ключу и проверить допустимость значения.

    Удобная функция, объединяющая поиск параметра и проверку значения
    в одном вызове (без изменения самого параметра). Если параметр не
    найден, возвращает False.
    """
    parameter = find_parameter(parameters, setting_id, key)
    if parameter is None:
        return False
    return validate_parameter_value(parameter, value)


def validate_parameter_value(parameter: dict, value: ParameterValue) -> bool:
    """Проверить, допустимо ли значение для данного параметра."""
    value_type = parameter["value_type"]
    if value_type == "int":
        if not isinstance(value, int) or isinstance(value, bool):
            return False
        min_value = parameter.get("min_value")
        max_value = parameter.get("max_value")
        if min_value is not None and value < min_value:
            return False
        if max_value is not None and value > max_value:
            return False
        return True
    if value_type == "bool":
        return isinstance(value, bool)
    if value_type == "str":
        if not isinstance(value, str):
            return False
        allowed_values = parameter.get("allowed_values")
        if allowed_values is not None:
            return value in allowed_values
        return True
    return False


def get_parameter_status(is_valid: bool) -> str:
    """Вернуть текстовый статус параметра."""
    if is_valid:
        return "Значение параметра допустимо"
    return "Недопустимое значение параметра"


def update_parameter_value(
    parameters: List[dict],
    setting_id: int,
    key: str,
    new_value: ParameterValue,
) -> bool:
    """Изменить значение параметра, если оно допустимо."""
    parameter = find_parameter(parameters, setting_id, key)
    if parameter is None:
        raise KeyError(f"Параметр '{key}' не найден.")
    if not validate_parameter_value(parameter, new_value):
        return False
    parameter["value"] = new_value
    return True


def reset_parameter_to_default(
    parameters: List[dict],
    setting_id: int,
    key: str,
) -> bool:
    """Сбросить параметр к значению по умолчанию."""
    parameter = find_parameter(parameters, setting_id, key)
    if parameter is None:
        return False
    parameter["value"] = parameter["default_value"]
    return True


def show_parameters(parameters: List[dict]) -> None:
    """Вывести список параметров."""
    if not parameters:
        print("Параметры не найдены.")
        return
    for parameter in parameters:
        print(f"[{parameter['id']}] {parameter['key']} = {parameter['value']}")


def filter_parameters_by_type(
    parameters: List[dict],
    value_type: str,
) -> Iterator[dict]:
    """Отобрать параметры заданного типа.

    Реализовано как генератор: значения формируются по мере
    необходимости, без построения промежуточного списка.
    """
    for parameter in parameters:
        if parameter["value_type"] == value_type:
            yield parameter


def sort_parameters_by_key(parameters: List[dict]) -> List[dict]:
    """Вернуть параметры, отсортированные по ключу (lambda-функция)."""
    return sorted(parameters, key=lambda parameter: parameter["key"])
