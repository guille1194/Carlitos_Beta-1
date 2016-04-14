from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from .forms import UserRegistrationForm, ContactForm
from django.core.urlresolvers import reverse_lazy
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'Carlos_Home/home.html')

def about(request):
    return render(request, 'Carlos_Home/about.html')

class RegisterUser(FormView):
    template_name = 'Carlos_Home/register_user.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('Carlos_Home/home')

    def form_valid(self, form):
        user = form.save()
        p = Usuario()
        p.user_perfil = user
        p.mail = form.cleaned_data['mail']
        p.phone = form.cleaned_data['phone']
        p.save()
        return super(RegisterUser,self).form_valid(form)

class ContactView(FormView):
    template_name = 'Carlos_Home/contact.html'
    form_class = ContactForm
    success_url = ('Carlos_Home/home')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
