from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from .forms import  ContactForm
from django.core.urlresolvers import reverse_lazy

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
