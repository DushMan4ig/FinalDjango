from django.contrib import admin
from .apps import Profile

# Отображение модели Profile в админке проекта
admin.site.register(Profile)