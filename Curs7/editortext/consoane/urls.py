from django.urls import path
from .views import consoane_view

urlpatterns = [

	path("numarare/", consoane_view),
]
