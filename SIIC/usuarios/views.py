from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .form import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from .models import Usuario
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.


class UsuarioCreate(GroupRequiredMixin, CreateView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    template_name = "cadastros/form_user.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        # cria o usuario no grupo correspondente
        grupo = get_object_or_404(Group, name="Padrão")
        # antes do supero o objeto da classe não foi criado
        url = super().form_valid(form)
        # objeto criado
        self.object.groups.add(grupo)
        self.object.save()

        # criando perfil
        # Perfil.objects.create(usuario=self.object)
        return url

    # método que pode ser utilizado em formulários padrão para passar o título
    # personalizado
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo_pagina"] = "Cadastrar usuário"
        context['titulo'] = 'Registro de novo usuário'
        return context


class PerfilUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/form.html'
    model = Usuario
    fields = ['nome_completo', 'email', 'telefone']
    success_url = reverse_lazy('inicio')

    # metodo para pegart o usuário sem ser pelo pk na url
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Usuario, username=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo_pagina"] = "Atualizar perfil"
        context["titulo"] = 'Dados pessoais'
        context["botao"] = 'atualizar'
        return context

# metodo para alteração de senha do usuário logado


def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('inicio')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'usuarios/alterar_senha.html', {'form_senha': form_senha})
