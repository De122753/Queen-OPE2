from django.shortcuts import render
from django.http.response import HttpResponse
import relatorio.forms as r

# Create your views here.
def relatorio_movimento(request):
    template_name = 'relatorio_movimento.html'
    campos = r.Relatorio()
    context = {'campos_relatorio': campos}
    return render(request,template_name, context)