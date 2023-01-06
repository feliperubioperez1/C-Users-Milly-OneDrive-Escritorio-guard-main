from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    activo = models.BooleanField()
    def __str__(self):
        return self.nombre

class Guardias(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    rut = models.CharField(max_length=12)
    activo = models.BooleanField()
    foto = models.ImageField(upload_to="fotos",null=False)
    empresas = models.ForeignKey(Empresa,on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre