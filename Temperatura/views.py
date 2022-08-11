from django.shortcuts import render

def Escalas(request):
  return render(request, 'escalas.html', context={})

