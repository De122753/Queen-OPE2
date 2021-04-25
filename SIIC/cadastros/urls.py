from django.urls import path
from .views import PedidoCreate
from .views import UsuarioUpdate, PedidoUpdate, ProdutoUpdate
from .views import UsuarioDelete, PedidoDelete, ProdutoDelete
from .views import UsuarioList, PedidoList, StatusCreate, CorCreate, TipoMovCreate, TamanhoProdutoCreate, ProdutoCreate, ItemCreate, ProdutoList, ProdutoDetalhes

# from .views import IndexView


urlpatterns = [
    path('cadastrar/pedido', PedidoCreate.as_view(), name='cadastrar-pedido'),

    # UPDATE -- OBTEM O ID ATRAVÉS DA URL
    path('editar/usuario/<int:pk>/',
         UsuarioUpdate.as_view(), name='editar-usuario'),
    path('editar/pedido/<int:pk>/', PedidoUpdate.as_view(),  name='editar-pedido'),
    path('editar/produto/<int:pk>', ProdutoUpdate.as_view(), name='editar-produto'),

    path('cadastrar/status', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/cor', CorCreate.as_view(), name='cadastrar-cor'),
    path('cadastrar/movimentacao', TipoMovCreate.as_view(),
         name='cadastrar-movimentacao'),
    path('cadastrar/tamanho', TamanhoProdutoCreate.as_view(),
         name='cadastrar-tamanho'),
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/item', ItemCreate.as_view(), name='cadastrar-item'),

    # DELETE -- OBTEM O ID ATRAVÉS DA URL
    path('excluir/usuario/<int:pk>/',
         UsuarioDelete.as_view(), name='excluir-usuario'),
    path('excluir/pedido/<int:pk>/',
         PedidoDelete.as_view(),  name='excluir-pedido'),
    path('excluir/produto/<int:pk>',
         ProdutoDelete.as_view(), name='excluir-produto'),

    # LISTAR BANCO
    path('listar/usuarios/', UsuarioList.as_view(), name='listar-usuarios'),
    path('listar/pedidos/', PedidoList.as_view(), name='listar-pedidos'),
    path('listar/produtos/', ProdutoList.as_view(), name='listar-produtos'),
    path('<int:pk>/', ProdutoDetalhes, name='detalhar-produto'),
]
