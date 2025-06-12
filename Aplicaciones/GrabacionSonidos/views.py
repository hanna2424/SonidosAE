from django.shortcuts import render, redirect
from .models import GrabacionSonido, EspecieSonido
from django.contrib import messages

# Lista de grabaciones
def inicioGrabacionSonido(request):
    grabaciones = GrabacionSonido.objects.all()
    return render(request, "inicioGrabacionSonido.html", {'grabaciones': grabaciones})


# Formulario nueva grabación
def nuevaGrabacionSonido(request):
    especies_sonido = EspecieSonido.objects.all()
    return render(request, "nuevaGrabacionSonido.html", {'especies_sonido': especies_sonido})


# Guardar nueva grabación
def guardarGrabacionSonido(request):
    especie_sonido_id = request.POST["especie_sonido"]
    fecha = request.POST["fecha"]
    ubicacion = request.POST["ubicacion"]
    archivo_audio = request.FILES.get("archivo_audio")

    especie_sonido = EspecieSonido.objects.get(id=especie_sonido_id)
    nueva = GrabacionSonido.objects.create(
        especie_sonido=especie_sonido,
        fecha=fecha,
        ubicacion=ubicacion,
        archivo_audio=archivo_audio
    )
    messages.success(request, "Grabación registrada exitosamente")
    return redirect('/grabacionsonido')


# Eliminar grabación
def eliminarGrabacionSonido(request, id):
    obj = GrabacionSonido.objects.get(id=id)
    obj.delete()
    messages.success(request, "Grabación eliminada exitosamente")
    return redirect('/grabacionsonido')


# Formulario edición
def editarGrabacionSonido(request, id):
    grabacion = GrabacionSonido.objects.get(id=id)
    especies_sonido = EspecieSonido.objects.all()
    return render(request, "editarGrabacionSonido.html", {
        'grabacion': grabacion,
        'especies_sonido': especies_sonido
    })


# Procesar edición
def procesarEdicionGrabacionSonido(request, id):
    especie_sonido_id = request.POST["especie_sonido"]
    fecha = request.POST["fecha"]
    ubicacion = request.POST["ubicacion"]
    archivo_audio = request.FILES.get("archivo_audio")

    especie_sonido = EspecieSonido.objects.get(id=especie_sonido_id)
    obj = GrabacionSonido.objects.get(id=id)
    obj.especie_sonido = especie_sonido
    obj.fecha = fecha
    obj.ubicacion = ubicacion
    if archivo_audio:
        obj.archivo_audio = archivo_audio
    obj.save()

    messages.success(request, "Grabación actualizada exitosamente")
    return redirect('/grabacionsonido')
