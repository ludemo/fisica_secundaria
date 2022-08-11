from django.urls import include, path
from . import views

urlpatterns = [
  path("escalas", views.Escalas, name="escalas"),
]