

from django.contrib import admin
from django.urls import path, include

from .views import factorial_view

## URLS din matematica (APLICATIE)

urlpatterns = [
    path('<int:n>', factorial_view),
]
