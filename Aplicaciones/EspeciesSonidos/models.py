from django.db import models
from Aplicaciones.Especies.models import Especie 

# Create your models here.
class EspecieSonido(models.Model):
    id = models.AutoField(primary_key=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    tipo_sonido = models.CharField(max_length=100)
    descripcion = models.TextField()
    pdf_estudio = models.FileField(upload_to='pdf_estudios/', null=True, blank=True)

    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id, self.especie.nombre, self.tipo_sonido)
