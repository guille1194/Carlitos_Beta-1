from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
<<<<<<< HEAD
=======
from django.core.validators import MaxValueValidator, MinValueValidator
>>>>>>> 076cb5b75f09415052a5e9d2ac594143d9c5f767

# Create your models here.
class Cursos(models.Model):
    ID_Curso = models.AutoField(primary_key=True)
    #numero_curso = models.IntegerField(unique=True)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return self.curso

class Categoria(models.Model):
    ID_Categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    #orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    ID_Post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 200)
    contenido = models.TextField()
    #slug = models.SlugField(unique=True)
    categorias = models.ForeignKey(Categoria)
    post_imagen = models.ImageField(upload_to='post_imagen/')
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(default=timezone.now)
    post_video = models.CharField(max_length = 300, null = True)

    def __str__(self):
        return self.titulo

class Profesionista(models.Model):
    ID_Profesionista = models.AutoField(primary_key=True)
    perfil_usuario = models.OneToOneField(User)
    nombre_profesionista = models.CharField(max_length = 68)
    apellido_profesionista = models.CharField(max_length = 68)
    REPORTES = (
        ('SI', 'Si'),
        ('NO', 'No'),
    )
    reportes = models.CharField(max_length = 2, choices=REPORTES)
    horario_inicio = models.TimeField()
    horario_final = models.TimeField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    telefono = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    curso = models.ForeignKey(Cursos)
    email = models.EmailField()

    def __unicode__(self):
        return(self.curso)

    def __str__(self):
        return 'nombre: %s - curso: %s' %(self.nombre_profesionista, self.curso)

class Paciente(models.Model):
    ID_Paciente = models.AutoField(primary_key=True)
    perfil_usuario = models.OneToOneField(User)
    nombre_paciente = models.CharField(max_length = 99)
    apellido_paciente = models.CharField(max_length = 99)
    num_expediente = models.IntegerField() #ocupo saber como manejan el numero de expediente
    area = models.CharField(max_length = 30) # esto no viene siendo lo mismo que los cursos?
    fecha_ingreso = models.DateField(default=timezone.now)
    fecha_conclusion = models.DateField(default=timezone.now)
    EVALUACION = (
        ('SI', 'Si'),
        ('NO', 'No'),
    )
    evaluacion_completa = models.CharField(max_length = 2, choices=EVALUACION)
    REPORTES = (
        ('SI', 'Si'),
        ('NO', 'No'),
    )
    reportes = models.CharField(max_length = 2, choices=REPORTES)
    diagnostico = models.CharField(max_length = 45)
    fecha_nacimiento = models.DateField(default=timezone.now)
    edad_ingreso = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(130)])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    telefono = models.IntegerField(validators=[phone_regex], blank=True, max_length=15)
    email = models.EmailField()
    GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero = models.CharField(max_length=1, choices=GENERO)


    def __str__(self):
        return 'nombre: %s - numero expediente: %d - edad ingreso: %d' %(self.nombre_paciente, num_expediente, edad_ingreso)
<<<<<<< HEAD
=======

class Perfil(models.Model):
    ID_Perfil = models.AutoField(primary_key=True)
	perfil_usuario = models.OneToOneField(User)
	email = models.EmailField()
>>>>>>> 076cb5b75f09415052a5e9d2ac594143d9c5f767
