"""Класс параметра настройки."""

from typing import Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .settings import Setting

ParameterValue = Union[str, int, bool]


class Parameter:
    """Именованное значение настройки с проверкой допустимости."""

    def __init__(
        self,
        parameter_id: int,
        setting: "Setting",
        key: str,
        value: ParameterValue,
        value_type: str,
        default_value: ParameterValue,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None,
        allowed_values: Optional[list] = None,
    ) -> None:
        """Создать объект параметра."""
        self.id = parameter_id
        self.setting = setting
        self.key = key
        self.value = value
        self.value_type = value_type
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value
        self.allowed_values = allowed_values

    def is_valid_value(self, value: ParameterValue) -> bool:
        """Проверить, допустимо ли значение для данного параметра."""
        if self.value_type == "int":
            if not isinstance(value, int) or isinstance(value, bool):
                return False
            if self.min_value is not None and value < self.min_value:
                return False
            if self.max_value is not None and value > self.max_value:
                return False
            return True
        if self.value_type == "bool":
            return isinstance(value, bool)
        if self.value_type == "str":
            if not isinstance(value, str):
                return False
            if self.allowed_values is not None:
                return value in self.allowed_values
            return True
        return False

    def update_value(self, new_value: ParameterValue) -> bool:
        """Изменить значение параметра, если оно допустимо."""
        if not self.is_valid_value(new_value):
            return False
        self.value = new_value
        return True

    def reset_to_default(self) -> None:
        """Сбросить параметр к значению по умолчанию."""
        self.value = self.default_value

    def __str__(self) -> str:
        """Вернуть строковое представление параметра."""
        return f"{self.key} = {self.value}"

    @staticmethod
    def validate_type(value: ParameterValue, value_type: str) -> bool:
        """Проверить соответствие значения базовому типу параметра."""
        if value_type == "int":
            return isinstance(value, int) and not isinstance(value, bool)
        if value_type == "bool":
            return isinstance(value, bool)
        if value_type == "str":
            return isinstance(value, str)
        return False
