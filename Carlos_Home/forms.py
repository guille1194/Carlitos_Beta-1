from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cursos

class ContactForm(forms.Form):
    name = forms.CharField()
    emal = forms.CharField();
    message = forms.CharField(widget = forms.Textarea)

    def send_email(self):
        pass

class RegistroCursoForm(forms.Form):
    numero_curso = forms.IntegerField()
    curso = forms.CharField(max_length=50)

class ProfesionistaForm(UserCreationForm):
    reportes = forms.CharField()
    HORARIO = (
                    ('M', 'Matutino'),
                    ('V', 'Vespertino'),
                )
    horario = forms.ChoiceField(choices = HORARIO)
    telefono = forms.IntegerField()
    curso = forms.ModelChoiceField(Cursos.objects.values_list('curso'), empty_label= "Selecciona Curso")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class PacienteForm(UserCreationForm):
    num_expediente = forms.IntegerField()
    area = forms.CharField()
    fecha_ingreso = forms.DateField(input_formats = ['%m/%d/%y'])
    fecha_conclusion = forms.DateField(input_formats = ['%m/%d/%y'])
    evaluacion_completa = forms.CharField()
    reportes = forms.CharField()
    diagnostico = forms.CharField()
    fecha_nacimiento = forms.DateField(input_formats = ['%m/%d/%y'])
    edad_ingreso = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    ELECCION_GENERO = (
                    ('M', 'Masculino'),
                    ('F', 'Femenino'),
                    )
    genero = forms.ChoiceField(choices=ELECCION_GENERO)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
