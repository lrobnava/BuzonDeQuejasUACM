from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quejas

# Create your views here.
def Index(request):
    return HttpResponse("<h1>Bienvenido UACM Avisos</h1>")

def BuzonQuejas(request):
    alert_message = ""
    if request.method == "GET":
        return render(request, "pages/index.html", {"alert_message" : None})
    else:
        name = request.POST['nombre']
        type = request.POST['motivo']
        contain = request.POST['contenido']
        alert_message = "Tu comentario o queja a sido enviado con éxito!"
        queja = Quejas.objects.create(user=name, type = type, quejaText = contain)
    return render(request, "pages/index.html", {'alert_message': alert_message})


def Queja(request):
    alert_message = request.GET.get('alert_message')
    return render(request, "pages/index.html", {'alert_message': alert_message})


