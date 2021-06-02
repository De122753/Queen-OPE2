from django.shortcuts import render
from django.http.response import HttpResponse
import relatorio.forms as r
from reportlab.pdfgen import canvas
from .models import TOTAL_PRODUTOS
from datetime import datetime
from django.db.models import Sum, OrderBy
import decimal



# Retorna a pagina do relatorio de movimetno e dados do DB
def relatorio_movimento(request):
    
    if request.method=='POST':
        dataInicio = request.POST['dataInicio']
        dataFim = request.POST['dataFim']

        template_name = 'relatorio_movimento.html'
        ##Primeiro resumo
        qtd_entrada = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio,dataFim),
                                MOVIMENTO='ENTRADA').aggregate(Sum('QUANTIDADE')).values())[0]
        
        qtd_saida = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio,dataFim),
                                MOVIMENTO='SAIDA').aggregate(Sum('QUANTIDADE')).values())[0]

        ##Segundo resumo
        total_entrada = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio,dataFim),
                                MOVIMENTO='ENTRADA').aggregate(Sum('TOTAL')).values())[0]
        total_saida = list(TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio,dataFim),
                                MOVIMENTO='SAIDA').aggregate(Sum('TOTAL')).values())[0]
        
        if total_entrada == None:
            template_name = 'relatorio_movimento.html'
            return render(request,template_name)

        campos_resumo = total_saida - total_entrada
        
        ##Tabela Movimentações dos Produtos - Analítico
        campos_produtos = TOTAL_PRODUTOS.objects.filter(CREATED__range=(dataInicio,dataFim)).order_by('CREATED')
        context = {

            'campos_resumo': campos_resumo,
            'campos_produtos': campos_produtos,
            'total_entrada': total_entrada,
            'total_saida': total_saida,
            'qtd_entrada': qtd_entrada,
            'qtd_saida': qtd_saida,
            'dataInicio': dataInicio,
            'dataFim': dataFim,
            
        }
        return render(request, template_name, context)

    else:
        template_name = 'relatorio_movimento.html'
        return render(request,template_name)


def pdf(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(mimetype='application/pdf')
    response['relatorio-movimento'] = 'attachment; filename=relatório_movimento.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(100, 100, "Hello world.")

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()
    return response


   