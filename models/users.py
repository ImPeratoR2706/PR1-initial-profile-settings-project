"""Класс пользователя системы."""


class User:
    """Пользователь системы."""

    def __init__(self, user_id: int, username: str, email: str) -> None:
        """Создать объект пользователя."""
        self.id = user_id
        self.username = username
        self.email = email

    def __str__(self) -> str:
        """Вернуть строковое представление пользователя."""
        return f"{self.username} ({self.email})"

    @classmethod
    def from_data(cls, data: dict) -> "User":
        """Создать пользователя из набора данных."""
        return cls(data["id"], data["username"], data["email"])
