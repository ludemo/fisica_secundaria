from django.shortcuts import render

def Vectores(request):
  return render(request, 'vectores.html', context={})
