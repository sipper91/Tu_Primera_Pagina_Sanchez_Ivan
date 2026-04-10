from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

class UserEditForm(forms.ModelForm):
    imagen = forms.ImageField(label="Foto de Perfil (Avatar)", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        
        help_texts = {
            'username': None,
        }
