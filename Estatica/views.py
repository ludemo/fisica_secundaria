from django.shortcuts import render
from django.http import HttpResponseRedirect
import numpy as np
import math

def Estatica(request):
  return render(request, 'estatica.html', context={})

def Leyes_de_newton(request):
  return render(request, 'leyes_de_newton.html', context={})

def Fuerza_friccion(request):
  return render(request, 'fuerzas_friccion.html', context={})


def estatica_calculadora(request):
    if request.method == "GET":
        if request.GET.get('a'):
            rpt_a = request.GET.get('a')
            rpt_b = request.GET.get('b')
            return render(request, "calculadora-estatica.html", context={'a': rpt_a, 'b': rpt_b})

        return render(request, "calculadora-estatica.html", context={'a': '', 'b': ''})
    elif request.method == "POST":
        gr_a = request.POST.get('gr_a')
        gr_b = request.POST.get('gr_b')
        w = request.POST.get('w')
        rpta = None
        if gr_a == '0':
            rpta = sta_T(int(w), -1, 0, math.cos(np.radians(int(gr_b))),math.sin(np.radians(int(gr_b))))
        else :
            rpta = sta_T(int(w), -math.cos(np.radians(int(gr_a))), math.sin(np.radians(int(gr_a))), math.cos(np.radians(int(gr_b))),math.sin(np.radians(int(gr_b))))
        return HttpResponseRedirect('/estatica/calculadora/?a='+str(rpta[0])+'&b='+str(rpta[1]))

    
def sta_T(W, Ax, Ay, Bx, By):
    sys_m = np.array([[Ax,Bx], [Ay, By]])
    sys_n = np.array([0, W])
    return np.linalg.inv(sys_m).dot(sys_n)

