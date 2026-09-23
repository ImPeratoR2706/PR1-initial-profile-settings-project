"""Класс профиля пользователя."""

from typing import List, Optional, TYPE_CHECKING

from .users import User

if TYPE_CHECKING:
    from .settings import Setting


class Profile:
    """Профиль пользователя: именованный набор настроек."""

    def __init__(
        self,
        profile_id: int,
        user: User,
        name: str,
        description: str,
    ) -> None:
        """Создать объект профиля."""
        self.id = profile_id
        self.user = user
        self.name = name
        self.description = description
        self.settings: List["Setting"] = []

    def add_setting(self, setting: "Setting") -> None:
        """Добавить настройку в профиль."""
        self.settings.append(setting)

    def find_setting(self, category: str) -> Optional["Setting"]:
        """Найти настройку профиля по категории."""
        for setting in self.settings:
            if setting.category == category:
                return setting
        return None

    def __str__(self) -> str:
        """Вернуть строковое представление профиля."""
        return (
            f"{self.name} (владелец: {self.user.username}), "
            f"настроек: {len(self.settings)}"
        )
