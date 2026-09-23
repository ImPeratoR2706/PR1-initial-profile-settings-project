"""Класс настройки профиля."""

from typing import List, Optional, TYPE_CHECKING

from .profiles import Profile

if TYPE_CHECKING:
    from .parameters import Parameter


class Setting:
    """Настройка: категория параметров профиля."""

    def __init__(
        self,
        setting_id: int,
        profile: Profile,
        category: str,
    ) -> None:
        """Создать объект настройки."""
        self.id = setting_id
        self.profile = profile
        self.category = category
        self.parameters: List["Parameter"] = []

    def add_parameter(self, parameter: "Parameter") -> None:
        """Добавить параметр в настройку."""
        self.parameters.append(parameter)

    def find_parameter(self, key: str) -> Optional["Parameter"]:
        """Найти параметр настройки по ключу."""
        for parameter in self.parameters:
            if parameter.key == key:
                return parameter
        return None

    def __str__(self) -> str:
        """Вернуть строковое представление настройки."""
        return (
            f"{self.category} (профиль «{self.profile.name}»), "
            f"параметров: {len(self.parameters)}"
        )
