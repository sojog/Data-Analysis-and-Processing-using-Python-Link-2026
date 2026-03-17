from django.urls import path
from .views import inserare_view
from .views import consoane_view

urlpatterns = [

	path("numarare/", consoane_view),
	path("inserare", inserare_view),
]
