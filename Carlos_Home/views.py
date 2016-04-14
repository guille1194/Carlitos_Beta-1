from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from .forms import  ContactForm, RegistroCursoForm, ProfesionistaForm
from django.core.urlresolvers import reverse_lazy
from .models import Cursos, Profesionista

# Create your views here.

def home(request):
    return render(request, 'Carlos_Home/home.html')

def about(request):
    return render(request, 'Carlos_Home/about.html')

class ContactView(FormView):
    template_name = 'Carlos_Home/contact.html'
    form_class = ContactForm
    success_url = ('Carlos_Home/home')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

def Registros(request):
    return render(request, 'Carlos_Home/Registros.html')

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
        return super(ProfesionitaView,self).form_valid(form)

def admin(request):
    return render(request, 'Carlos_Home/Admin.html')
