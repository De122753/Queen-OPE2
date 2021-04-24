# FORMULÁRIO PADRÃO DO DJANGO E ALTERAÇÕES DIVERSAS

# from SIIC.usuarios.models import Perfil
# from SIIC.usuarios.models import Usuario
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
# from .models import Perfil


class UsuarioForm(UserCreationForm):
    # campo para personalização do formulário padrão
    # nome_completo = forms.CharField(max_length=100)

    class Meta:
        model = Usuario
        fields = ['username', 'nome_completo', 'cpf', 'telefone', 'email', 'password1', 'password2']
