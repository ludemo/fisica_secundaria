from django.shortcuts import render

def Dinamica(request):
  return render(request, 'dinamica.html', context={})
