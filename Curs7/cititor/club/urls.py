from django.urls import path
from .views import validare_cnp_view_post_view
from .views import validare_cnp_view

urlpatterns = [

	path("cnp", validare_cnp_view),
	path("cnppost", validare_cnp_view_post_view),
]
