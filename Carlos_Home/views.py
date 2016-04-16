from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from .forms import  ContactForm, RegistroCursoForm, ProfesionistaForm, PacienteForm
from django.core.urlresolvers import reverse_lazy
from .models import Cursos, Profesionista, Paciente, Post, Categoria
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'Carlos_Home/home.html')

def about(request):
    return render(request, 'Carlos_Home/about.html')

class ContactView(FormView):
    template_name = 'Carlos_Home/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form_email = form.cleaned_data.get('emal')
        form_message = form.cleaned_data.get('message')
        form_name = form.cleaned_data.get('name')

        subject = 'Test Mailbox'
        contact_message ='%s: %s Via: %s'%(form_name,form_message,form_email)
        from_email = settings.EMAIL_HOST_USER
        to_email =[from_email]
        send_mail(subject, contact_message, from_email,to_email, fail_silently=False)
        return super(ContactView, self).form_valid(form)



def Registros(request):
    return render(request, 'Carlos_Home/Registros.html')

def Reportes(request):
    return render(request, 'Carlos_Home/Reportes.html')

class CursoView(FormView):
    template_name = 'Carlos_Home/Registro_curso.html'
    form_class = RegistroCursoForm
    success_url = reverse_lazy('registros_view')

    def form_valid(self, form):
        p = Cursos()
        p.numero_curso = form.cleaned_data['numero_curso']
        p.curso = form.cleaned_data['curso']
        p.save()
        return super(CursoView,self).form_valid(form)

class ProfesionitaView(FormView):
    template_name = 'Carlos_Home/Registro_prof.html'
    form_class = ProfesionistaForm
    success_url = reverse_lazy('registros_view')

    def form_valid(self,form):
        user = form.save()
        p = Profesionista()
        p.perfil_usuario = user
        p.nombre_profesionista = user.first_name
        p.apellido_profesionista = user.last_name
        p.reportes = form.cleaned_data['reportes']
        p.horario = form.cleaned_data['horario']
        p.telefono = form.cleaned_data['telefono']
        p.curso = form.cleaned_data['curso']
        p.email = form.cleaned_data['email']
        p.save()
        return super(ProfesionitaView,self).form_valid(form)

def admin(request):
    return render(request, 'Carlos_Home/Admin.html')

class PacienteView(FormView):
    template_name = 'Carlos_Home/Registro_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('registros_view')

    def form_valid(self,form):
        user = form.save()
        p = Paciente()
        p.perfil_usuario = user
        p.nombre_paciente = user.first_name
        p.apellido_paciente = user.last_name
        p.num_expediente = form.cleaned_data['num_expediente']
        p.area = form.cleaned_data['area']
        p.fecha_ingreso = form.cleaned_data['fecha_ingreso']
        p.fecha_conclusion = form.cleaned_data['fecha_conclusion']
        p.evaluacion_completa = form.cleaned_data['evaluacion_completa']
        p.reportes = form.cleaned_data['reportes']
        p.diagnostico = form.cleaned_data['diagnostico']
        p.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
        p.edad_ingreso = form.cleaned_data['edad_ingreso']
        p.telefono = form.cleaned_data['telefono']
        p.email = form.cleaned_data['email']
        p.genero = form.cleaned_data['genero']
        p.save()
        return super(PacienteView,self).form_valid(form)

class ReportePaciente(ListView):
	template_name = 'Carlos_Home/reporte_paciente.html'
	model = Paciente
	fields = '__all__'

class ReporteProfesionista(ListView):
	template_name = 'Carlos_Home/reporte_profesionista.html'
	model = Profesionista
	fields = '__all__'

class ReporteCurso(ListView):
	template_name = 'Carlos_Home/reporte_cursos.html'
	model = Cursos
	fields = '__all__'

class Crear_Post(CreateView):
	template_name = 'Carlos_Home/CrearPost.html'
	model = Post
	fields = '__all__'
	success_url=reverse_lazy('index_view')

class Crear_Categoria(CreateView):
    template_name='Carlos_Home/CrearCategoria.html'
    model = Categoria
    fields= '__all__'
    success_url=reverse_lazy('index_view')

def post_detalle(request, id=None):
	post = get_object_or_404(Post, id=id)
	context = {
		"object_list": "eee",
		"post": post,
	}
	return render(request, "Carlos_Home/post_detalle.html", context)

def post_lista(request):
	queryset_list = Post.objects.all().order_by('-creado')
	paginator = Paginator(queryset_list, 3) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset
	}
	return render(request, "Carlos_Home/post_lista.html", context)
