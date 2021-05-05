from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def relatorio_movimento(request):
    template_name = 'relatorio_movimento.html'
    return render(request,template_name)