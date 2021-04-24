from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from usuarios.models import Usuario

# Create your views here.

# lista de usuarios django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import CorProduto, Pedido, StatusPedido, TipoMovimentacao, TamanhoProduto, Produto, Item

# Controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# ##################################### CREATE #################################


class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['data_fechamento', 'nota_fiscal', 'pedido_ususario',
              'status_pedido', 'tipo_movimentacao', 'frete', 'valor_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')

    # Metodo para registrar o usuário que realiza o pedido
    def form_valid(self, form):
        # referencia o usuário da clásse no models
        form.instance.usuario_pedido = self.request.user
        # antes do supero o objeto da classe não foi criado
        url = super().form_valid(form)
        # objeto criado
        # Adicionar um texto ao campo
        # self.object.valor += "[qualquercoisa]"
        # self.object.save()
        return url

    # Efetua a substituição no HTML dos termos constantes nos argumentos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de pedidos"
        context["titulo"] = "Novo pedido"
        context["subtitulo"] = "Cadastro de pedidos para compra/venda de produdos"
        context["botao"] = "Cadastrar"
        return context


class StatusCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = StatusPedido
    fields = ['status_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.usuario_pedido = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de status"
        context["titulo"] = "Cadastrar novo status de pedidos"
        context["subtitulo"] = "Cadastro de status"
        context["botao"] = "Cadastrar"
        return context


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


class TipoMovCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = TipoMovimentacao
    fields = ['tipo_movimentacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.usuario_pedido = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de movimentação"
        context["titulo"] = "Cadastrar novo tipo de movimentação"
        context["subtitulo"] = "Cadastro de movimentações"
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
    fields = ['nome_produto', 'descricao_produto', 'preco_unitario', 'quantidade_disponivel', 'tamanho_produto', 'cor_produto']
    template_name = 'cadastros/form_produto.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de produto"
        context ['titulo'] = 'Cadastrar novo produto'
        context ['subtitulo'] = 'Cadastro de produtos'
        context ['botao'] = 'Cadastrar'
        return context


class ItemCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Item
    fields = ['quantidade_item ', 'desconto', 'valor_item', 'produto', 'pedido']
    template_name = 'cadastros/form.html'
    success_url =  reverse_lazy('inicio')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de item"
        context ['titulo'] = 'Cadastrar novo item'
        context ['subtitulo'] = 'Cadastro de itens'
        context ['botao'] = 'Cadastrar'
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


class PedidoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Usuario
    fields = ['valor_pedido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Atualizar pedido"
        context["titulo"] = "Editar pedidos"
        context["subtitulo"] = "Editar pedidos cadastrados no SIIC"
        context["botao"] = "Editar"
        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome_produto', 'descricao_produto', 'preco_unitario', 'tamanho_produto', 'cor_produto', 'quantidade_disponivel']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Atualizar produto"
        context["titulo"] = "Editar produtos"
        context["subtitulo"] = "Editar produtos cadastrados no SIIC"
        context["botao"] = "Editar"
        return context

# ##################################### DELETE #################################


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy(GroupRequiredMixin, LoginRequiredMixin, 'login')
    group_required = u"Adm"
    model = Usuario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-usuarios')


class PedidoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pedidos')


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


class PedidoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Adm", u"Padrão"]    
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/listas/pedidos.html'

class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/produtos.html'