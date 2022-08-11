from django.urls import include, path
from . import views

urlpatterns = [
  path("", views.Electrodinamica, name="electrodinamica"),
  path("ley_ohm", views.Ley_ohm, name="ley_ohm"),
]