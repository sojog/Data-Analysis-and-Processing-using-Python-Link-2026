from django.contrib import admin
from django.urls import path, include

from .views import random_number_view, six_random_numbers_view

## URLS din matematica (APLICATIE)

urlpatterns = [
    path('random/', random_number_view),
    path('extragere/', six_random_numbers_view)
]
