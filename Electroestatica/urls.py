from django.urls import include, path
from . import views

urlpatterns = [
  path("", views.Electroestatica, name="electroestatica"),
  path("ley_coulomb", views.Ley_coulomb, name="ley_coulomb"),
]