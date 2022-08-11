from django.urls import include, path
from . import views

urlpatterns = [
  path("", views.Estatica, name="estatica"),
  path("leyes_de_newton/", views.Leyes_de_newton, name="leyes_de_newton"),
  path("fuerzas_friccion/", views.Fuerza_friccion, name="fuerzas_friccion"),
]