from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Curso, Categoria

class ContactForm(forms.Form):
    name = forms.CharField()
    emal = forms.CharField();
    message = forms.CharField(widget = forms.Textarea)

    def send_email(self):
        pass

class RegistroCursoForm(forms.Form):
    curso = forms.CharField(max_length = 30)
    desc = forms.CharField(max_length = 200)
    costo = forms.CharField(max_length = 50)
    horario_inicio = forms.TimeField()
    horario_final = forms.TimeField()
    fecha = forms.DateField()
    imgen = forms.ImageField()

class ProfesionistaForm(UserCreationForm):
    REPORTES = (
    ('SI', 'Si'),
    ('NO', 'No'),
    )
    reportes = forms.ChoiceField(choices = REPORTES)
    horario_inicio = forms.TimeField()
    horario_final = forms.TimeField()
    telefono = forms.IntegerField()
    curso = forms.ModelChoiceField(Curso.objects, empty_label= "Selecciona Curso")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class PacienteForm(forms.Form):
    nombre_paciente = forms.CharField(max_length = 30)
    apellido_paciente = forms.CharField(max_length = 30)
    num_expediente = forms.IntegerField()
    AREAS = (
        ('lenguaje', 'Lenguaje'),
        ('aprendizaje', 'Aprendisaje'),
        ('psicologia', 'Psicologia'),
    )
    area = forms.ChoiceField(choices = AREAS)
    fecha_ingreso = forms.DateField()
    fecha_conclusion = forms.DateField()
    Opciones = (
        ('SI', 'Si'),
        ('NO', 'No'),
    )
    evaluacion_completa = forms.ChoiceField(choices=Opciones)
    reportes = forms.ChoiceField(choices=Opciones)
    diagnostico = forms.CharField()
    fecha_nacimiento = forms.DateField()
    edad_ingreso = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    ELECCION_GENERO = (
                    ('M', 'Masculino'),
                    ('F', 'Femenino'),
                    )
    genero = forms.ChoiceField(choices=ELECCION_GENERO)


class User_form(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1','password2']

class PostForm(forms.Form):
    titulo = forms.CharField()
    contenido = forms.CharField(widget=forms.Textarea)
    slug = forms.SlugField()
    categorias = forms.ModelChoiceField(Categoria.objects.values_list('nombre'),  empty_label= "Selecciona Curso")
    post_imagen = forms.ImageField()
    creado = forms.DateTimeField(input_formats = ['%m/%d/%Y %H:%M:%S'])
    post_video = forms.CharField()
