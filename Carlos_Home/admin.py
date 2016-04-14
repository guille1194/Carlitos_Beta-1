from django.contrib import admin
from .models import Paciente, Profesionista, Cursos

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Profesionista)
admin.site.register(Cursos)
