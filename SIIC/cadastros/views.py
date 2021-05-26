from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.shortcuts import render
# Create your views here.

# lista de usuarios django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import CorProduto, TamanhoProduto, Produto, Categoria

# Controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# ##################################### CREATE #################################


class CorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = CorProduto
    fields = ['cor_produto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.usuario_pedido = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de cor"
        context["titulo"] = "Cadastrar nova cor de produto"
        context["subtitulo"] = "Cadastro de cores"
        context["botao"] = "Cadastrar"
        return context


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.usuario_pedido = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de categorias"
        context["titulo"] = "Cadastrar nova categoria de produto"
        context["subtitulo"] = "Cadastro de categorias"
        context["botao"] = "Cadastrar"
        return context


class TamanhoProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = TamanhoProduto
    fields = ['tamanho_produto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.usuario_pedido = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de tamanho"
        context["titulo"] = "Cadastrar novo tamanho de produto"
        context["subtitulo"] = "Cadastro de tamanhos"
        context["botao"] = "Cadastrar"
        return context


class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('Login')
    model = Produto
    fields = ['nome_produto', 'descricao_produto', 'preco_unitario',
              'quantidade_disponivel', 'tamanho_produto', 'cor_produto', 'categoria', 'foto']
    template_name = 'cadastros/form_produto.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de produto"
        context['titulo'] = 'Cadastrar novo produto'
        context['subtitulo'] = 'Cadastro de produtos'
        context['botao'] = 'Cadastrar'
        return context

    # ##################################### UPDATE #################################


class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['username', 'email', 'nome_completo', 'cpf', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-usuarios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo_pagina"] = "Atualizar usuário"
        context["titulo"] = 'Atualizar dados do usuário'
        context["botao"] = 'atualizar'
        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome_produto', 'descricao_produto', 'preco_unitario',
              'tamanho_produto', 'cor_produto', 'quantidade_disponivel', 'categoria', 'foto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Atualizar produto"
        context["titulo"] = "Editar produtos"
        context["subtitulo"] = "Editar produtos cadastrados no SIIC"
        context["botao"] = "Salvar edição"

        return context

# ##################################### DELETE #################################


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy(GroupRequiredMixin, LoginRequiredMixin, 'login')
    group_required = u"Adm"
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-usuarios')


class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')

# #########################LISTAR OBJETOS DE UM BANCO ##########################


class UsuarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/listas/usuarios.html'


class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/produtos.html'


def ProdutoDetalhes(request, pk):
    obj = Produto.objects.get(pk=pk)
    template_name = 'cadastros/listas/detalhe_produto.html'
    context = {'object': obj}
    return render(request, template_name, context)


def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
