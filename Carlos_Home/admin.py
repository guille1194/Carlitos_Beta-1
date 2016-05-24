from django.contrib import admin
from .models import Paciente, Profesionista, Curso, Paciente, Post, Categoria
# Register your models here.


admin.site.register(Paciente)
admin.site.register(Profesionista)
admin.site.register(Curso)
admin.site.register(Categoria)
admin.site.register(Post)
