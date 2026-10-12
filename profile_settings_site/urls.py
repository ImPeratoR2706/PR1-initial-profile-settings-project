"""
URL configuration for profile_settings_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("profiles/", include("profiles.urls")),
    path("settings/", include("settings.urls")),
]

handler404 = "homepage.views.page_not_found"
