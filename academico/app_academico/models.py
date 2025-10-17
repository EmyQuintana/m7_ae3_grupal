from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from estudiantes.models import Estudiante
from cursos.models import Curso

ESTADO_CHOICES = [
    ('activo', 'Activo'),
    ('finalizado', 'Finalizado'),
]


# Create your models here.
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    fecha_inscripcion=models.DateField(auto_now_add=True)
    estado=models.CharField (
        max_length=20,
        choices= ESTADO_CHOICES,
        default='activo',
    )
    nota_final= models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    class Meta:
        unique_together = ('estudiante', 'curso')   
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return f"{self.estudiante.nombre.capitalize()} {self.estudiante.apellido} - {self.curso.nombre}"