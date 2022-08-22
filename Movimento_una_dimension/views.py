from django.shortcuts import render
from .metodos.mru import mru_distance, mru_time, mru_velocity

def Movimiento_una_dimension(request):
  return render(request, 'movimiento_una_dimension.html', context={})
def MRUV(request):
  return render(request, 'MRUV.html', context={})


def MRU(request):
  context = {}
  if request.POST:
    velocity = request.POST.get('velocidad', False)
    print(velocity)
    time = request.POST.get('tiempo', False)
    distance = request.POST.get('distancia', False)
    context = mru_distance(velocity, time)
  return render(request, 'MRU.html', context=context)

def Caida_libre(request):
  return render(request, 'caida_libre.html', context={})