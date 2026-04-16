from django.db import models

class Asistencia(models.Model):
    nombre_completo = models.CharField(max_length=150)
    documento = models.CharField(max_length=50)
    correo = models.EmailField()
    fecha = models.DateField()
    hora_ingreso = models.TimeField()
    hora_salida = models.TimeField()
    presente = models.BooleanField()
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_completo