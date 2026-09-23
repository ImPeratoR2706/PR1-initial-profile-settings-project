"""Вспомогательные функции безопасного ввода данных."""


def input_int(prompt: str) -> int:
    """Запросить у пользователя целое число.

    При некорректном вводе запрос повторяется.
    """
    while True:
        raw_value = input(prompt)
        try:
            return int(raw_value)
        except ValueError:
            print("Ошибка: введите целое число.")


def input_choice(prompt: str, options: list) -> str:
    """Запросить у пользователя один из допустимых вариантов.

    При некорректном вводе запрос повторяется.
    """
    while True:
        raw_value = input(prompt).strip()
        if raw_value in options:
            return raw_value
        print(f"Ошибка: допустимые значения - {', '.join(options)}.")
