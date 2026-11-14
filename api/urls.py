from django.urls import path
from . import views


urlpatterns = [
    path("registros/", views.registro_list),


    path('usuarios/', views.usuario_list),
    path('usuarios/<int:pk>', views.usuario_detail)
]
