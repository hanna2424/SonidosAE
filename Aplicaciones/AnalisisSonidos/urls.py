from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioAnalisisSonido),
    path('nuevoAnalisisSonido', views.nuevoAnalisisSonido),
    path('guardarAnalisisSonido', views.guardarAnalisisSonido),
    path('eliminarAnalisisSonido/<id>', views.eliminarAnalisisSonido),
    path('editarAnalisisSonido/<id>', views.editarAnalisisSonido),
    path('procesarEdicionAnalisisSonido/<id>', views.procesarEdicionAnalisisSonido),
]
