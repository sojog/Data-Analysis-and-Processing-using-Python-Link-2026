from django.urls import path
from .views import food_view

urlpatterns = [

	path("food", food_view),
]
