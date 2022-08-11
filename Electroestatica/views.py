from django.shortcuts import render

def Electroestatica(request):
  return render(request, 'electroestatica.html', context={})

def Ley_coulomb(request):
  return render(request, 'ley_coulumb.html', context={})
