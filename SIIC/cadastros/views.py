from django.core.checks import messages
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from usuarios.models import Usuario
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# lista de usuarios django
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .models import CorProduto, TamanhoProduto, Produto, Categoria, Fornecedor
from .forms import CorForm

# Controle de login
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


# ##################################### CREATE #################################


class CorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = CorProduto
    fields = ['cor_produto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-produto')

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


def salva_cor(request):
    cor_produto = request.POST.get('cor_produto')
    count = CorProduto.objects.filter(cor_produto=cor_produto).count()  # contar cores
    if count > 0:
        # messages.error(request, 'Já cadastrada.')
        messages.add_message(request, messages.SUCCESS, 'Cor já cadastrada no sistema!')
        return redirect('cadastrar-produto')
    else:
        form = CorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar-produto')


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastrar-produto')

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
    success_url = reverse_lazy('cadastrar-produto')

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


class ProdutoCreate(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    login_url = reverse_lazy('Login')
    model = Produto
    fields = ['nome_produto', 'descricao_produto', 'preco_unitario',
              'quantidade_disponivel', 'tamanho_produto', 'cor_produto', 'peso', 'categoria', 'ncm', 'fabricante', 'localizacao', 'estoque_minimo',  'foto']
    template_name = 'cadastros/form_produto.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, "Cadastro do produto realizado com sucesso!")
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro de produto"
        context['titulo'] = 'Cadastrar novo produto'
        context['subtitulo'] = 'Cadastro de produtos'
        context['botao'] = 'Cadastrar'
        return context


class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('Login')
    model = Fornecedor
    fields = ['nome_fornecedor',
              'nome_fornecedor_redizido',
              'cnpj_fornecedor',
              'logradouro_fornecedor',
              'numero_via_fornecedor',
              'cidade_fornecedor',
              'uf_fornecedor',
              'contato_fornecedor',
              'email_fornecedor',
              'telefone_fornecedor'
              ]
    template_name = 'cadastros/form_fornecedor.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, "Fornecedor cadastrado com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Cadastro fornecedor"
        context['titulo'] = 'Cadastrar novo fornecedor/fabricante'
        context['subtitulo'] = 'Cadastro de fornecedor/fabricante'
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

    def form_valid(self, form):
        messages.success(self.request, "Alteração realizada com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo_pagina"] = "Atualizar usuário"
        context["titulo"] = 'Atualizar dados do usuário'
        context["botao"] = 'atualizar'
        return context


class FornecedorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Adm"
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nome_fornecedor',
              'nome_fornecedor_redizido',
              'cnpj_fornecedor',
              'logradouro_fornecedor',
              'numero_via_fornecedor',
              'cidade_fornecedor',
              'uf_fornecedor',
              'contato_fornecedor',
              'email_fornecedor',
              'telefone_fornecedor'
              ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedores')

    def form_valid(self, form):
        messages.success(self.request, "Alteração realizada com sucesso!")
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo_pagina"] = "Atualizar fornecedor"
        context["titulo"] = 'Atualizar dados do fornecedor'
        context["botao"] = 'atualizar'
        return context


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome_produto', 'descricao_produto', 'preco_unitario',
              'tamanho_produto', 'cor_produto', 'quantidade_disponivel', 'categoria', 'peso', 'ncm', 'fabricante', 'localizacao', 'estoque_minimo', 'foto']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def form_valid(self, form):
        messages.success(self.request, "Alteração realizada com sucesso!")
        return super().form_valid(form)

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


class FornecedorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = [u"Adm", u"Padrão"]
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/listas/fornecedores.html'


def ProdutoDetalhes(request, pk):
    obj = Produto.objects.get(pk=pk)
    template_name = 'cadastros/listas/detalhe_produto.html'
    context = {'object': obj}
    return render(request, template_name, context)


def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
