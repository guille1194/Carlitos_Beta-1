from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Paciente, Profesionista, Cursos, Paciente, Post, Categoria
# Register your models here.

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Paciente)
admin.site.register(Profesionista)
admin.site.register(Cursos)
admin.site.register(Categoria)
admin.site.register(Post, PostAdmin)
