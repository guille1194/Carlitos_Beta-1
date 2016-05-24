from django.conf.urls import url
from .views import home, about, ContactView, Registros, Reportes, CursoView, ProfesionitaView, admin, PacienteView, ReporteProfesionista, ReportePaciente, ReporteCurso, Crear_Post, post_detalle, post_lista, Crear_Categoria, BlogAdmin, Registro, Cursos, test, Blog
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^$', login, {'template_name': 'Carlos_Home/home.html'}, name='login'),
	url(r'^cerrar/$', logout_then_login, name='logout'),
    url(r'^$', home, name= "home"),
    url(r'^about/$',about, name = "about_view"),
    url(r'^contacto$', ContactView.as_view(), name = "contacto"),
    url(r'^registros$', Registros, name = "registros_view"),
    url(r'^reportes$', Reportes, name = "reportes_view"),
    url(r'^registro_curso$', CursoView.as_view(), name = "CursoView_view" ),
    url(r'^registro_profesionista$',ProfesionitaView.as_view(), name = "ProfesionitaView_view"),
    url(r'^panel_admin$', admin, name = "admin_panel"),
    url(r'^registro_paciente$', PacienteView.as_view(), name = "PacienteView_view"),
    url(r'^ReporteProfesionista/$', ReporteProfesionista.as_view(), name='reporte_profesionista_view'),
	url(r'^ReportePaciente/$', ReportePaciente.as_view(), name='reporte_paciente_view'),
    url(r'^ReporteCurso/$', ReporteCurso.as_view(), name='reporte_curso_view'),
    url(r'^Crear_Post/$', Crear_Post.as_view(), name='crear_post_view'),
    url(r'^post_detalle/(?P<id>\d+)/$', post_detalle, name='post_detalle'),
    url(r'^post_lista/$', post_lista, name='post_lista'),
    url(r'^Crear_Categoria/$', Crear_Categoria.as_view(), name='crear_categoria_view'),
    url(r'^blogadmin/$', BlogAdmin, name= "blog_admin"),
    url(r'^registro/$', Registro.as_view(), name='registro_view'),
	url(r'^cursos/$', Cursos.as_view(), name = "cursos_view"),
	url(r'^test/$', test, name = "test_view"),
	url(r'^blog/$', Blog.as_view(), name = 'blog' )
]
