from django.shortcuts import render

def Electrodinamica(request):
  return render(request, 'electrodinamica.html', context={})

def Ley_ohm(request):
  return render(request, 'ley_ohm.html', context={})

