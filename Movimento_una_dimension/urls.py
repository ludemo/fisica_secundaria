from django.urls import include, path
from . import views

urlpatterns = [
  path("", views.Movimiento_una_dimension, name="movimiento_una_dimension"),
  path("MRUV/", views.MRUV, name="MRUV"),
  path("MRU/", views.MRU, name="MRU"),
  path("caida_libre/", views.Caida_libre, name="caida_libre")
]