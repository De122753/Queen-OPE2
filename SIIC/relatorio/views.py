from django.shortcuts import render
from django.http.response import HttpResponse
import relatorio.forms as r
from reportlab.pdfgen import canvas
from .models import TOTAL_PRODUTOS
from django.db.models import Sum, OrderBy
from django.contrib import messages
from datetime import timedelta, datetime, date


# Retorna a pagina do relatorio de movimetno e dados do DB
def relatorio_movimento(request):

    if request.method == 'POST':
        dtini = request.POST['dataInicio']
        dtfim = request.POST['dataFim']

        dI = datetime.strptime(dtini, '%Y-%m-%d').date()
        dF = datetime.strptime(dtfim, '%Y-%m-%d').date()

        dataInicio = dI - timedelta(days=1)
        dataFim = dF + timedelta(days=1)

        template_name = 'relatorio_movimento.html'
        # Primeiro resumo
        qtd_entrada = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim),
                                                         MOVIMENTO='ENTRADA').aggregate(Sum('QUANTIDADE')).values())[0]
        qtd_saida = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim),
                                                       MOVIMENTO='SAIDA').aggregate(Sum('QUANTIDADE')).values())[0]
        qtd_baixa = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim),
                                                       MOVIMENTO='BAIXA').aggregate(Sum('QUANTIDADE')).values())[0]

        # Segundo resumo round(float( , 2)
        total_entrada = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim),
                                                           MOVIMENTO='ENTRADA').aggregate(Sum('TOTAL')).values())[0]
        total_saida = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim),
                                                         MOVIMENTO='SAIDA').aggregate(Sum('TOTAL')).values())[0]
        total_baixa = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim),
                                                         MOVIMENTO='BAIXA').aggregate(Sum('TOTAL')).values())[0]

        if total_entrada == None and total_saida == None and total_baixa == None:
            template_name = 'relatorio_movimento.html'
            return render(request, template_name, messages.warning(request, 'Não consta dados no período, por favor, selecione uma nova data.'))

        campos_resumo = (total_saida - total_entrada) - total_baixa

        # Tabela Movimentações dos Produtos - Analítico
        campos_produtos = TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio, dataFim)).order_by('CREATED')
        context = {

            'campos_resumo': campos_resumo,
            'campos_produtos': campos_produtos,
            'total_entrada': total_entrada,
            'total_saida': total_saida,
            'total_baixa': total_baixa,
            'qtd_entrada': qtd_entrada,
            'qtd_saida': qtd_saida,
            'qtd_baixa': qtd_baixa,
            'dataInicio': dtini,
            'dataFim': dtfim,

        }
        return render(request, template_name, context)

    else:
        template_name = 'relatorio_movimento.html'
        return render(request, template_name)


# class HelloPDFView(PDFTemplateView):
#     template_name = "hello.html"
