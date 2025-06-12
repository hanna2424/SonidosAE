from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioEspecieSonido),
    path('nuevaEspecieSonido', views.nuevaEspecieSonido),
    path('guardarEspecieSonido', views.guardarEspecieSonido),
    path('eliminarEspecieSonido/<id>', views.eliminarEspecieSonido),
    path('editarEspecieSonido/<id>', views.editarEspecieSonido),
    path('procesarEdicionEspecieSonido/<id>', views.procesarEdicionEspecieSonido),
]
