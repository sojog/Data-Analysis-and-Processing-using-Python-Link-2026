from django.contrib import admin
from django.urls import path, include


from .views import random_color_view, hex_color_view

## URL - intern (din aplicatie)
urlpatterns = [
    path('color/', random_color_view),
    path('<hexcolor>/', hex_color_view)
]
