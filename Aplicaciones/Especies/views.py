from django.shortcuts import render, redirect
from .models import Especie
from django.contrib import messages

# Create your views here.
def inicioEspecie(request):
    listadoEspecies = Especie.objects.all()
    return render(request, "inicioEspecie.html", {'especies': listadoEspecies})


def nuevaEspecie(request):
    return render(request, "nuevaEspecie.html")


def guardarEspecie(request):
    nombre = request.POST["nombre"]
    tipo_especie = request.POST["tipo_especie"]
    nueva = Especie.objects.create(nombre=nombre, tipo_especie=tipo_especie)
    messages.success(request, "Especie agregada exitosamente")
    return redirect('/especie')


def eliminarEspecie(request, id):
    especieEliminar = Especie.objects.get(id=id)
    especieEliminar.delete()
    messages.success(request, "Especie eliminada exitosamente")
    return redirect('/especie')


def editarEspecie(request, id):
    especieEditar = Especie.objects.get(id=id)
    return render(request, "editarEspecie.html", {'especieEditar': especieEditar})


def procesarEdicionEspecie(request, id):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    tipo_especie = request.POST["tipo_especie"]

    especie = Especie.objects.get(id=id)
    especie.nombre = nombre
    especie.tipo_especie = tipo_especie
    especie.save()
    messages.success(request, "Especie actualizada exitosamente")
    return redirect('/especie')
