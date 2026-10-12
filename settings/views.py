from django.http import HttpResponse

from homepage.views import page
from storage import (
    find_setting_by_id,
    load_parameters,
    load_profiles,
    load_settings,
    load_users,
)


def setting_list(request):
    """Список всех настроек всех профилей."""
    users = load_users("data/users.json")
    profiles = load_profiles("data/profiles.json", users)
    all_settings = load_settings("data/settings.json", profiles)
    load_parameters("data/parameters.json", all_settings)

    items = ""
    for setting in all_settings:
        items += (
            '<li class="list-group-item d-flex '
            'justify-content-between align-items-center">'
            f'<a href="/settings/{setting.id}/">'
            f'{setting.category} - {setting.profile.name}</a>'
            f'<span class="badge bg-secondary">'
            f'параметров: {len(setting.parameters)}'
            f'</span></li>'
        )
    content = f"""
    <h1>Настройки</h1>
    <p>Всего настроек: {len(all_settings)}</p>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Настройки профилей", content))


def setting_detail(request, setting_id):
    """Страница отдельной настройки со списком её параметров."""
    users = load_users("data/users.json")
    profiles = load_profiles("data/profiles.json", users)
    all_settings = load_settings("data/settings.json", profiles)
    load_parameters("data/parameters.json", all_settings)

    setting = find_setting_by_id(all_settings, setting_id)

    if setting is None:
        content = """
        <h1 class="text-danger">Настройка не найдена</h1>
        <p>Настройка с указанным идентификатором отсутствует.</p>
        <a href="/settings/" class="btn btn-outline-secondary">
            ← к списку настроек
        </a>
        """
        return HttpResponse(
            page("Настройка не найдена", content),
            status=404,
        )

    parameter_items = ""
    for parameter in setting.parameters:
        if parameter.value == parameter.default_value:
            badge = '<span class="badge bg-success">по умолчанию</span>'
        else:
            badge = (
                '<span class="badge bg-warning text-dark">изменено</span>'
            )
        parameter_items += (
            '<li class="list-group-item d-flex '
            'justify-content-between align-items-center">'
            f'<span><strong>{parameter.key}</strong>: {parameter.value} '
            f'<small class="text-muted">({parameter.value_type})</small>'
            f'</span>{badge}</li>'
        )
    if not parameter_items:
        parameter_items = (
            '<li class="list-group-item">'
            "У настройки пока нет параметров."
            "</li>"
        )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h1 class="card-title">{setting.category}</h1>
            <p class="card-text"><strong>ID:</strong> {setting.id}</p>
            <p class="card-text">
                <strong>Профиль:</strong>
                <a href="/profiles/{setting.profile.id}/">
                    {setting.profile.name}
                </a>
            </p>
            <h2 class="h5 mt-4">Параметры настройки</h2>
            <ul class="list-group">{parameter_items}</ul>
            <a href="/settings/" class="btn btn-outline-secondary mt-3">
                ← к списку настроек
            </a>
        </div>
    </div>
    """
    return HttpResponse(
        page(f"{setting.category} - настройка", content),
        status=200,
    )
