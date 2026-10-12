from django.urls import path

from . import views

app_name = "settings"

urlpatterns = [
    path("", views.setting_list, name="list"),
    path("<int:setting_id>/", views.setting_detail, name="detail"),
]
