from django.shortcuts import render
from django.http.response import HttpResponse
import relatorio.forms as r
from reportlab.pdfgen import canvas
from .models import TOTAL_PRODUTOS, TOTALIZADOR, RESUMO_FINANC


# Retorna a pagina do relatorio de movimetno e dados do DB
def relatorio_movimento(request):
    template_name = 'relatorio_movimento.html'
    campos_produtos = TOTAL_PRODUTOS.objects.all()
    campos_resultado = TOTALIZADOR.objects.all()
    campos_resumo = '-57.236,00'
    context = {'campos_total': campos_resultado,'campos_relatorio': campos_produtos, 'campos_resumo':campos_resumo}
    return render(request, template_name, context)

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


