from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    mail = forms.EmailField(required = True)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('__all__')
        exclude = ['last_login','is_superuser','password','groups','user_permissions','email','is_staff','is_active','date_joined',]

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)

    def send_email(self):
        pass 
