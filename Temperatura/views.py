from django.shortcuts import render
from django.http import HttpResponseRedirect
def Escalas(request):
  return render(request, 'escalas.html', context={})

def temperatura_calculadora(request):
    if request.method == "GET":
        if request.GET.get('rpta'):
            rpta = request.GET.get('rpta')
            return render(request, "calculadora-temperatura.html", context={'rpta': rpta})

        return render(request, "calculadora-temperatura.html", context={'rpta': ''})
    elif request.method == "POST":
        m = float(request.POST.get('m'))
        c = float(request.POST.get('c'))
        vt = float(request.POST.get('vt'))
        rpta = m*c*vt
        
        return HttpResponseRedirect('/temperatura/calculadora/?rpta='+str(rpta))

def home(request):
    return render(request, 'temperatura-home.html', context={})
