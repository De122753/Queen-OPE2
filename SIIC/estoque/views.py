from django.db.models.expressions import Value
from django.forms import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import Estoque, EstoqueItens, EstoqueEntrada, EstoqueSaida
from .forms import EstoqueIntensForm, EstoqueForm
from cadastros.models import Produto
from cadastros.forms import ProdutoForm
from django.forms import forms


def estoque_entrada_list(request):
    template_name = 'estoque_list.html'
    objects = EstoqueEntrada.objects.all()
    context = {
        'object_list': objects,
        'titulo_list': 'ENTRADA DE ITENS NO ESTOQUE',
        'url_list_add': 'estoque_entrada_add',
        'detalhes': 'detalhar-itens'
    }
    return render(request, template_name, context)


def estoque_entrada_detalhes(request, pk):
    obj = EstoqueEntrada.objects.get(pk=pk)
    template_name = 'estoque_detalhes.html'
    context = {
        'object': obj,
        'url_list': 'estoque_entrada_list',
        'botao_listas': 'Lista de entradas',
        'titulo_detalhe': 'ENTRADA - DETALHES DO ITEM'
    }
    return render(request, template_name, context)


def dar_baixa_estoque(form):

    # Pega os produtos a partir da instância do formulário (Estoque).
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.quantidade_disponivel = item.saldo
        produto.preco_unitario = item.preco_unit
        # calcula o valor do item antes de salvar
        produto.valor_item = item.calcula_total
        # produto.valor_item_total = item.total_geral_item()
        produto.save()
    print('Estoque atualizado com sucesso.')


def estoque_add(request, template_name, movimento, url):
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueIntensForm,
        extra=0,
        min_num=1,
        validate_min=True,
        can_delete=True

    )
    if request.method == 'POST':
        form = EstoqueForm(
            request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(
            request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.save()
            formset.save()
            dar_baixa_estoque(form)
            return {'pk': form.pk}
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    context = {'form': form, 'formset': formset}
    return context


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    movimento = 'e'
    url = 'detalhar-itens'
    context = estoque_add(request, template_name, movimento, url,)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


def estoque_saida_list(request):
    template_name = 'estoque_list.html'
    objects = EstoqueSaida.objects.all()
    context = {
        'object_list': objects,
        'titulo_list': 'SAIDA DE ITENS DO ESTOQUE',
        'url_list_add': 'estoque_saida_add',
        'detalhes': 'detalhar-itens-saida'
    }
    return render(request, template_name, context)


def estoque_saida_detalhes(request, pk):
    obj = EstoqueSaida.objects.get(pk=pk)
    template_name = 'estoque_detalhes.html'
    context = {
        'object': obj,
        'url_list': 'estoque_saida_list',
        'botao_listas': 'Lista de saídas',
        'titulo_detalhe': 'SAÍDA - DETALHES DO ITEM'
    }
    return render(request, template_name, context)


def estoque_saida_add(request):
    template_name = 'estoque_saida_form.html'
    movimento = 's'
    url = 'detalhar-itens-saida'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)
