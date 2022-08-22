from django.urls import include, path
from . import views

urlpatterns = [
  path("", views.home, name='temperatura-home'),
  path("escalas", views.Escalas, name="escalas"),
  path("calculadora/", views.temperatura_calculadora, name='calculadora-temperatura'),
]
