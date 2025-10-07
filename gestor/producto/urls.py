from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("productos/", views.listado_productos, name="listado_productos"),
    path("solo-superuser/", views.solo_superuser, name="solo_superuser"),
]