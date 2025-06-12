from django.shortcuts import render, redirect
from .models import EspecieSonido, Especie
from django.contrib import messages

# Lista de todos los registros
def inicioEspecieSonido(request):
    listado = EspecieSonido.objects.all()
    return render(request, "inicioEspecieSonido.html", {'especiesonidos': listado})


# Formulario para nueva especie sonido
def nuevaEspecieSonido(request):
    especies = Especie.objects.all()  # Para el select
    return render(request, "nuevaEspecieSonido.html", {'especies': especies})


# Guardar el registro nuevo
def guardarEspecieSonido(request):
    especie_id = request.POST["especie"]
    tipo_sonido = request.POST["tipo_sonido"]
    descripcion = request.POST["descripcion"]
    pdf_estudio = request.FILES.get("pdf_estudio")

    especie = Especie.objects.get(id=especie_id)
    nueva = EspecieSonido.objects.create(
        especie=especie,
        tipo_sonido=tipo_sonido,
        descripcion=descripcion,
        pdf_estudio=pdf_estudio
    )
    messages.success(request, "Registro de especie-sonido agregado exitosamente")
    return redirect('/especiesonido')


# Eliminar registro
def eliminarEspecieSonido(request, id):
    obj = EspecieSonido.objects.get(id=id)
    obj.delete()
    messages.success(request, "Registro eliminado exitosamente")
    return redirect('/especiesonido')


# Formulario para edición
def editarEspecieSonido(request, id):
    registro = EspecieSonido.objects.get(id=id)
    especies = Especie.objects.all()
    return render(request, "editarEspecieSonido.html", {
        'registro': registro,
        'especies': especies
    })


# Procesar la edición
def procesarEdicionEspecieSonido(request, id):
    especie_id = request.POST["especie"]
    tipo_sonido = request.POST["tipo_sonido"]
    descripcion = request.POST["descripcion"]
    pdf_estudio = request.FILES.get("pdf_estudio")

    especie = Especie.objects.get(id=especie_id)
    obj = EspecieSonido.objects.get(id=id)
    obj.especie = especie
    obj.tipo_sonido = tipo_sonido
    obj.descripcion = descripcion
    if pdf_estudio:
        obj.pdf_estudio = pdf_estudio
    obj.save()

    messages.success(request, "Registro actualizado exitosamente")
    return redirect('/especiesonido')
