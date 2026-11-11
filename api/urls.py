from django.urls import path
from .views import registro_list


urlpatterns = [
    path("registros/", registro_list)
]
