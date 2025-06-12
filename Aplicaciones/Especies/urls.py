from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioEspecie),
    path('nuevaEspecie', views.nuevaEspecie),
    path('guardarEspecie', views.guardarEspecie),
    path('eliminarEspecie/<id>', views.eliminarEspecie),
    path('editarEspecie/<id>', views.editarEspecie),
    path('procesarEdicionEspecie/<id>', views.procesarEdicionEspecie),

]
