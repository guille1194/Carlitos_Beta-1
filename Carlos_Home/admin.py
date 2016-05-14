from django.contrib import admin
from .models import Paciente, Profesionista, Cursos, Paciente, Post, Categoria
# Register your models here.


admin.site.register(Paciente)
admin.site.register(Profesionista)
admin.site.register(Cursos)
admin.site.register(Categoria)
