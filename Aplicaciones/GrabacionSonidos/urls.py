from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioGrabacionSonido),
    path('nuevaGrabacionSonido', views.nuevaGrabacionSonido),
    path('guardarGrabacionSonido', views.guardarGrabacionSonido),
    path('eliminarGrabacionSonido/<id>', views.eliminarGrabacionSonido),
    path('editarGrabacionSonido/<id>', views.editarGrabacionSonido),
    path('procesarEdicionGrabacionSonido/<id>', views.procesarEdicionGrabacionSonido),
]
