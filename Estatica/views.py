from django.shortcuts import render

def Estatica(request):
  return render(request, 'estatica.html', context={})

def Leyes_de_newton(request):
  return render(request, 'leyes_de_newton.html', context={})

def Fuerza_friccion(request):
  return render(request, 'fuerzas_friccion.html', context={})