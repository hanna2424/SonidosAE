from django.shortcuts import render, redirect
from .models import AnalisisSonido, GrabacionSonido
from django.contrib import messages

# Lista de análisis
def inicioAnalisisSonido(request):
    analisis = AnalisisSonido.objects.all()
    return render(request, "inicioAnalisisSonido.html", {'analisis': analisis})


# Formulario nuevo análisis
def nuevoAnalisisSonido(request):
    grabaciones = GrabacionSonido.objects.all()
    return render(request, "nuevoAnalisisSonido.html", {'grabaciones': grabaciones})


# Guardar nuevo análisis
def guardarAnalisisSonido(request):
    grabacion_id = request.POST["grabacion"]
    investigador = request.POST["investigador"]
    fecha_analisis = request.POST["fecha_analisis"]
    observaciones = request.POST["observaciones"]
    pdf_resultados = request.FILES.get("pdf_resultados")

    grabacion = GrabacionSonido.objects.get(id=grabacion_id)
    nuevo = AnalisisSonido.objects.create(
        grabacion=grabacion,
        investigador=investigador,
        fecha_analisis=fecha_analisis,
        observaciones=observaciones,
        pdf_resultados=pdf_resultados
    )
    messages.success(request, "Análisis registrado exitosamente")
    return redirect('/analisissonido')


# Eliminar análisis
def eliminarAnalisisSonido(request, id):
    analisis = AnalisisSonido.objects.get(id=id)
    analisis.delete()
    messages.success(request, "Análisis eliminado exitosamente")
    return redirect('/analisissonido')


# Formulario edición
def editarAnalisisSonido(request, id):
    analisis = AnalisisSonido.objects.get(id=id)
    grabaciones = GrabacionSonido.objects.all()
    return render(request, "editarAnalisisSonido.html", {
        'analisis': analisis,
        'grabaciones': grabaciones
    })


# Procesar edición
def procesarEdicionAnalisisSonido(request, id):
    grabacion_id = request.POST["grabacion"]
    investigador = request.POST["investigador"]
    fecha_analisis = request.POST["fecha_analisis"]
    observaciones = request.POST["observaciones"]
    pdf_resultados = request.FILES.get("pdf_resultados")

    grabacion = GrabacionSonido.objects.get(id=grabacion_id)
    analisis = AnalisisSonido.objects.get(id=id)
    analisis.grabacion = grabacion
    analisis.investigador = investigador
    analisis.fecha_analisis = fecha_analisis
    analisis.observaciones = observaciones
    if pdf_resultados:
        analisis.pdf_resultados = pdf_resultados
    analisis.save()

    messages.success(request, "Análisis actualizado exitosamente")
    return redirect('/analisissonido')
