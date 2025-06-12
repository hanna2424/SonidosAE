from django.db import models

# Create your models here.
class Especie(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_especie = models.CharField(max_length=100)

    def __str__(self):
        fila= "{0}: {1} {2} "
        return fila.format(self.id, self.nombre,self.tipo_especie )
