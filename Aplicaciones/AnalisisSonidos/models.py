from django.db import models
from Aplicaciones.GrabacionSonidos.models import GrabacionSonido  

# Create your models here.
class AnalisisSonido(models.Model):
    id = models.AutoField(primary_key=True)
    grabacion = models.ForeignKey(GrabacionSonido, on_delete=models.CASCADE)
    investigador = models.CharField(max_length=100)
    fecha_analisis = models.DateField()
    observaciones = models.TextField()
    pdf_resultados = models.FileField(upload_to='resultados_pdf/', null=True, blank=True)

    def __str__(self):
        fila = "{0}: {1} - {2}"
        return fila.format(self.id, self.investigador, self.fecha_analisis)
