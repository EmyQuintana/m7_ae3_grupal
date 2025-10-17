# 📚 M7_AE3_GRUPAL: Modelado de Relaciones en Django

Este proyecto implementa y valida un modelo Entidad-Relación (ERD) académico utilizando el Object-Relational Mapper (ORM) de Django, con el objetivo de establecer y verificar las relaciones fundamentales: Uno a Uno (1:1), Uno a Muchos (1:M) y Muchos a Muchos (M:M), además de la regla de Borrado en Cascada (`CASCADE`).

---

## 👥 Integrantes del Equipo
**Emily Quintana** |
**Jorge Cárdenas** |

---

## 🏛️ Estructura de Modelos y Relaciones

El ejercicio se estructura en varias aplicaciones (`profesores`, `cursos`, `estudiantes`, `app_academico`) para gestionar las siguientes entidades y sus relaciones:

Modelo Principal	Relación	Modelo Secundario	Tipo de Relación
Profesor	           ↔	           Curso	    Uno a Muchos (1:M)
Estudiante	           ↔	           Perfil	    Uno a Uno (1:1)
Estudiante	           ↔	           Curso	    Muchos a Muchos (M:M)
Mediante	           →	           Inscripcion	(Tabla Intermedia con Datos Extra)
---

## 💻 Comandos de Validación en Django Shell

Los siguientes comandos se ejecutaron en el `python manage.py shell` para crear las entidades, establecer las relaciones y verificar el funcionamiento del `models.CASCADE`.

### 1. Preparación e Importación

```python
# Importar todos los modelos necesarios
>>> from profesores.models import Profesor
>>> from cursos.models import Curso
>>> from estudiantes.models import Estudiante, Perfil
>>> from app_academico.models import Inscripcion

# Crear Profesores
>>> p_ana = Profesor.objects.create(nombre='Ana', apellido='García', email='ana.g@uni.cl')
>>> p_beto = Profesor.objects.create(nombre='Beto', apellido='López', email='beto.l@uni.cl')

# Crear Estudiantes 
e_jose = Estudiante.objects.create(nombre='José', apellido='Torres',email='jose.t@uni.cl')

#Recuperar
>>> e_carlos = Estudiante.objects.get(apellido='Pérez')
>>> e_diana = Estudiante.objects.get(apellido='Rojas') 
>>> e_jose= Estudiante.objects.get(apellido='Torres')

# Crear Cursos y establecer 1:M (Profesor -> Curso)
>>> c_python = Curso.objects.create(nombre='Programación Python', profesor=p_beto)
>>> c_cuantica = Curso.objects.create(nombre='Física Cuántica', profesor=p_ana)

# Verificar 1:M (Relación Inversa)
>>> p_ana.cursos_impartidos.all()


# Crear Perfiles y establecer 1:1 (Estudiante -> Perfil)
# (Usando el campo rrss para las redes sociales)
>>> Perfil.objects.create(estudiante=e_carlos, biografia='Entusiasta de la ciencia...',rrss=({}))
>>> Perfil.objects.create(estudiante=e_jose, biografia='Estudiante nuevo, con gran interés en el desarrollo de software y la ciberseguridad.', 
rrss=({}))

# Verificar 1:1
>>> e_carlos.perfil.biografia

# Jose se inscribe en dos cursos
>>> Inscripcion.objects.create(estudiante=e_jose, curso=c_python)

>>> Inscripcion.objects.create(estudiante=e_carlos, curso=c_cuantica)

# Modificar el campo extra (nota_final)
>>> insc_jose_py = Inscripcion.objects.get(estudiante=e_jose, curso=c_python)
>>> insc_jose_py.nota_final = 6.0
>>> insc_jose_py.save()

#verificar notas
>>> print(f"La nota final de Jose en Python es: {insc_jose_py.nota_final}")

# Verificar M:M (Cursos de Carlos)
>>> e_carlos.cursos.all() 

# Crear y configurar el profesor de prueba (Clara)
>>> p_clara = Profesor.objects.create(nombre='Clara', apellido='Díaz', email='clara.d@uni.cl')
>>> c_ia = Curso.objects.create(nombre='Introducción a la IA', profesor=p_clara, creditos=5)
>>> Inscripcion.objects.create(estudiante=e_diana, curso=c_ia)

# Conteo ANTES del borrado
>>> print("Profesores antes:", Profesor.objects.count())
>>> print("Cursos antes:", Curso.objects.count()) 
>>> print("Inscripciones antes:", Inscripcion.objects.count()) 

# Ejecutar el CASCADE
>>> p_clara.delete() 

# Conteo DESPUÉS del borrado
>>> print("Profesores después:", Profesor.objects.count())
>>> print("Cursos después:", Curso.objects.count())
>>> print("Inscripciones después:", Inscripcion.objects.count())