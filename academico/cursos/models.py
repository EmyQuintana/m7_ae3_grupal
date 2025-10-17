from django.db import models
from profesores.models import Profesor
class Curso(models.Model): 
    profesor = models.ForeignKey(  #Un curso es impartido por un único profesor
        Profesor,
        on_delete=models.CASCADE, # borrar órdenes si se elimina el cliente
        related_name='cursos_impartidos',
    )
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Cursos"
   