from django.urls import path
from .views import cuvant_view
from .views import text_view

urlpatterns = [

	path("text/<text>", text_view),
	path("cuvant", cuvant_view),
]
