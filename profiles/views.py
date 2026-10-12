from django.http import HttpResponse

from homepage.views import page
from storage import (
    find_profile_by_id,
    load_profiles,
    load_settings,
    load_users,
)


def profile_list(request):
    """Список профилей пользователей."""
    users = load_users("data/users.json")
    profiles_list = load_profiles("data/profiles.json", users)
    load_settings("data/settings.json", profiles_list)

    items = ""
    for profile in profiles_list:
        items += (
            '<li class="list-group-item d-flex '
            'justify-content-between align-items-center">'
            f'<a href="/profiles/{profile.id}/">{profile.name}</a>'
            f'<span class="badge bg-secondary">'
            f'владелец: {profile.user.username}, '
            f'настроек: {len(profile.settings)}'
            f'</span></li>'
        )
    content = f"""
    <h1>Профили</h1>
    <p>Всего профилей: {len(profiles_list)}</p>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Профили - профили пользователей", content))


def profile_detail(request, profile_id):
    """Страница отдельного профиля со списком его настроек."""
    users = load_users("data/users.json")
    profiles_list = load_profiles("data/profiles.json", users)
    load_settings("data/settings.json", profiles_list)

    profile = find_profile_by_id(profiles_list, profile_id)

    if profile is None:
        content = """
        <h1 class="text-danger">Профиль не найден</h1>
        <p>Профиль с указанным идентификатором отсутствует.</p>
        <a href="/profiles/" class="btn btn-outline-secondary">
            ← к списку профилей
        </a>
        """
        return HttpResponse(
            page("Профиль не найден", content),
            status=404,
        )

    settings_items = "".join(
        f'<li class="list-group-item">{setting.category}</li>'
        for setting in profile.settings
    )
    if not settings_items:
        settings_items = (
            '<li class="list-group-item">У профиля пока нет настроек.</li>'
        )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h1 class="card-title">{profile.name}</h1>
            <p class="card-text"><strong>ID:</strong> {profile.id}</p>
            <p class="card-text">
                <strong>Владелец:</strong> {profile.user.username}
                ({profile.user.email})
            </p>
            <p class="card-text">
                {profile.description or "Без описания"}
            </p>
            <h2 class="h5 mt-4">Настройки профиля</h2>
            <ul class="list-group">{settings_items}</ul>
            <a href="/profiles/" class="btn btn-outline-secondary mt-3">
                ← к списку профилей
            </a>
        </div>
    </div>
    """
    return HttpResponse(
        page(f"{profile.name} - профиль", content),
        status=200,
    )
