from django.contrib import admin
from django.urls import path, include

from djapp.views import fridge_view, box_view, computer_view

urlpatterns = [
    path("inner/", computer_view)
]
