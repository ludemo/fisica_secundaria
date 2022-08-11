from django.urls import include, path
from . import views

urlpatterns = [
  path("", views.Teoria_relatividad, name="teoria_relatividad")
]