from django.shortcuts import render

def Movimiento_una_dimension(request):
  return render(request, 'movimiento_una_dimension.html', context={})

def MRUV(request):
  return render(request, 'MRUV.html', context={})

def MRU(request):
  return render(request, 'MRU.html', context={})

def Caida_libre(request):
  return render(request, 'caida_libre.html', context={})