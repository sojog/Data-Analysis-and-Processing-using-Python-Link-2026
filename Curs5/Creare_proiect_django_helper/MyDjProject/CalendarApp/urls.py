from django.urls import path
from .views import leap_years_view

urlpatterns = [

	path("leap/<int:start_year>/<int:stop_year>", leap_years_view),
]
