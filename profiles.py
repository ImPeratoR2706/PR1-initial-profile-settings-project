"""Функции для работы с профилями пользователей."""

from typing import List, Optional


def add_profile(
    profiles: List[dict],
    name: str,
    owner: str,
    description: str,
) -> dict:
    """Добавить профиль в коллекцию и вернуть созданную запись."""
    new_id = len(profiles) + 1
    profile = {
        "id": new_id,
        "name": name,
        "owner": owner,
        "description": description,
    }
    profiles.append(profile)
    return profile


def find_profile_by_id(
    profiles: List[dict],
    profile_id: int,
) -> Optional[dict]:
    """Найти профиль по идентификатору."""
    for profile in profiles:
        if profile["id"] == profile_id:
            return profile
    return None


def find_profiles_by_name(profiles: List[dict], query: str) -> List[dict]:
    """Найти профили, в названии которых встречается подстрока query."""
    query_lower = query.lower()
    return [
        profile for profile in profiles
        if query_lower in profile["name"].lower()
    ]


def sort_profiles(profiles: List[dict]) -> List[dict]:
    """Вернуть профили, отсортированные по названию."""
    return sorted(profiles, key=lambda profile: profile["name"])


def show_profiles(profiles: List[dict]) -> None:
    """Вывести список профилей."""
    if not profiles:
        print("Профили не найдены.")
        return
    for profile in profiles:
        print(
            f"[{profile['id']}] {profile['name']} "
            f"(владелец: {profile['owner']}) - {profile['description']}"
        )
