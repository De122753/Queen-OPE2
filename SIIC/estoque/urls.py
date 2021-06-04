from django.db import models
from django.urls.conf import path
# , estoque_entrada_add
from .views import *

# tabela_completa


urlpatterns = [
    path('estoque/listar_entradas', estoque_entrada_list, name='estoque_entrada_list'),
    path('estoque/listar_saidas', estoque_saida_list, name='estoque_saida_list'),
    path('estoque/listar_baixas', estoque_baixa_list, name='estoque_baixa_list'),
    path('estoque/itens_detalhados/', tabela_completa, name='estoque_itens_detalhados'),
    path('item_detalhe/<int:pk>/', estoque_entrada_detalhes, name='detalhar-itens'),
    path('item_baixa_detalhe/<int:pk>/', estoque_baixa_detalhes, name='detalhar-itens-baixa'),
    path('item_saida_detalhe/<int:pk>/', estoque_saida_detalhes, name='detalhar-itens-saida'),
    path('entrada/add/', estoque_entrada_add, name='estoque_entrada_add'),
    path('saida/add/', estoque_saida_add, name='estoque_saida_add'),
    path('baixa/add/', estoque_baixa_add, name='estoque_baixa_add'),
]
