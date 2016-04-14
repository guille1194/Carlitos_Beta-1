from django.contrib import admin
from .models import Paciente, Profesionista, Cursos, Usuario

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Profesionista)
admin.site.register(Cursos)
admin.site.register(Usuario)
