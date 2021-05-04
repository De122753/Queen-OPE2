from django.db import models
from django.urls.conf import path
# , estoque_entrada_add
from .views import estoque_entrada_list, estoque_entrada_detalhes, estoque_entrada_add


urlpatterns = [
    path('estoque/listar_entradas', estoque_entrada_list,
         name='estoque_entrada_list'),
    path('item_detalhe/<int:pk>/', estoque_entrada_detalhes, name='detalhar-itens'),
    path('add/', estoque_entrada_add, name='estoque_entrada_add'),
]
