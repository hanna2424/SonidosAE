from django.db import models
from Aplicaciones.EspeciesSonidos.models import EspecieSonido  

# Create your models here.
class GrabacionSonido(models.Model):
    id = models.AutoField(primary_key=True)
    especie_sonido = models.ForeignKey(EspecieSonido, on_delete=models.CASCADE)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    archivo_audio = models.FileField(upload_to='audios/', null=True, blank=True)

    def __str__(self):
        fila = "{0}: {1} - {2} - {3}"
        return fila.format(self.id, self.especie_sonido.tipo_sonido, self.fecha, self.ubicacion)
