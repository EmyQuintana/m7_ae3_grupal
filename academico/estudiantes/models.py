from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cursos.models import Curso

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    cursos = models.ManyToManyField(  #relacion muchos a muchos
        Curso,
        through='app_academico.inscripcion',
        related_name='estudiantes_inscritos',

    )
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class meta:
        verbose_name_plural = "Estudiantes"

class Perfil(models.Model):
    estudiante= models.OneToOneField(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    biografia = models.TextField(blank=True, null=True)
    foto=models.ImageField(upload_to="fotos")
    rrss=models.URLField()

    def __str__(self):
        return f"Perfil de {self.estudiante}"
    class meta:
        verbose_name_plural = "Perfiles"
    