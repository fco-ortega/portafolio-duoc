from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'email',
            'groups',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'groups': 'Seleccione un perfil de usuario',
        }

class UsuarioChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'groups',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'groups' : 'Seleccionar perfil de usuario',
        }