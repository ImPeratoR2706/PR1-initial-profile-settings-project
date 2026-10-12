from django.http import HttpResponse

BOOTSTRAP = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
    "/dist/css/bootstrap.min.css"
)


def page(title, content):
    """Собрать HTML-страницу с единым каркасом проекта.

    Функция подключает Bootstrap и навигационное меню, общие для всех
    страниц проекта. Используется всеми приложениями до перехода на
    систему шаблонов Django (см. ПР6).
    """
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{BOOTSTRAP}">
</head>
<body>
    <nav class="nav">
        <a class="nav-link" href="/">Главная</a>
        <a class="nav-link" href="/profiles/">Профили</a>
        <a class="nav-link" href="/settings/">Настройки</a>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def index(request):
    """Главная страница проекта."""
    content = """
    <h1 class="display-4">Система настройки пользовательских профилей</h1>
    <p class="lead">
        Веб-интерфейс индивидуального проекта: управление профилями
        пользователей, их настройками и параметрами.
    </p>
    <p>Основные разделы:</p>
    <a href="/profiles/" class="btn btn-primary me-2">Профили</a>
    <a href="/settings/" class="btn btn-secondary">Настройки</a>
    """
    return HttpResponse(page("Система настройки профилей", content))


def page_not_found(request, exception):
    """Обработчик ошибки 404: собственная страница проекта."""
    content = """
    <h1 class="text-danger">404 - страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 - страница не найдена", content),
        status=404,
    )
