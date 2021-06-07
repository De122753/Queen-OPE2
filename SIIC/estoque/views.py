
from datetime import datetime, timedelta
from django.db.models import query
from django.forms import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django_tables2 import tables
from django_tables2.config import RequestConfig
from .models import Estoque, EstoqueBaixa, EstoqueItens, EstoqueEntrada, EstoqueSaida, DetailedDataTable
from .forms import EstoqueIntensForm, EstoqueForm
from cadastros.models import Produto
from django_tables2.export.export import TableExport
import time
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .filters import ItensFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from dateutil.parser import parse


def estoque_entrada_list(request):
    template_name = 'estoque_list.html'
    objects = EstoqueEntrada.objects.all()
    context = {
        'object_list': objects,
        'titulo_list': 'ESTOQUE - ENTRADA DE ITENS',
        'url_list_add': 'estoque_entrada_add',
        'detalhes': 'detalhar-itens',
        'titulo': 'Movimentação - Entradas',
    }
    return render(request, template_name, context,)


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
        produto.valor_item = item.calcula_total
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
        can_delete=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(
            request.POST, request.FILES, instance=estoque_form, prefix='main')
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
    context = {'form': form, 'formset': formset, 'titulo': 'Adicionar itens'}
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
        'titulo_list': 'ESTOQUE - SAÍDA DE ITENS',
        'url_list_add': 'estoque_saida_add',
        'detalhes': 'detalhar-itens-saida',
        'titulo': 'Movimentação - Saidas',
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


def estoque_baixa_add(request):
    template_name = 'estoque_baixa_form.html'
    movimento = 'b'
    url = 'detalhar-itens-baixa'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


def estoque_baixa_detalhes(request, pk):
    obj = EstoqueBaixa.objects.get(pk=pk)
    template_name = 'estoque_detalhes.html'
    context = {
        'object': obj,
        'url_list': 'estoque_baixa_list',
        'botao_listas': 'Lista de baixas',
        'titulo_detalhe': 'BAIXA - DETALHES DO ITEM'
    }
    return render(request, template_name, context)


def estoque_baixa_list(request):
    template_name = 'estoque_list_baixa.html'
    objects = EstoqueBaixa.objects.all()
    context = {
        'object_list': objects,
        'titulo_list': 'ESTOQUE - BAIXA DE ITENS',
        'url_list_add': 'estoque_baixa_add',
        'detalhes': 'detalhar-itens-baixa',
        'titulo': 'Movimentação - Baixas',
    }
    return render(request, template_name, context)


def tabela_completa(request):
    template_name = 'estoque_list_full.html'
    q = EstoqueItens.objects.select_related().filter(estoque__created__date__gte=datetime.now()).order_by('estoque')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        print(start_date, end_date)
        q = EstoqueItens.objects.select_related().filter(estoque__created__date__range=[start_date, end_date]).order_by('estoque')
        table = DetailedDataTable(q)
        table = DetailedDataTable(q)
        context = {'table': table, }
        RequestConfig(request, paginate=False).configure(table)
        return render(request, template_name, context)

    table = DetailedDataTable(q)
    context = {'table': table, }
    RequestConfig(request, paginate=False).configure(table)
    return render(request, template_name, context)


# # filtro por classes

# class EstoqueFiltro(django_filters.FilterSet):
#     class Meta:
#         model = Estoque
#         fields = ['created']


# class TabelaDetalhada(SingleTableMixin, FilterView):
#     table_class = DetailedDataTable
#     model = Estoque
#     template_name = 'estoque_list_full.html'
#     filterset_class = EstoqueFiltro

# tabela detalhada com exportação


# class TabelaCompletaListView(SingleTableMixin, FilterView):
#     table_class = DetailedDataTable
#     model = Estoque
#     template_name = "estoque_list_full.html"
#     filterset_class = ItensFilter
