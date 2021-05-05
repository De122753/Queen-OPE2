from django.urls import path
from .views import UsuarioUpdate, ProdutoUpdate
from .views import UsuarioDelete, ProdutoDelete
from .views import UsuarioList, CorCreate, TamanhoProdutoCreate, ProdutoCreate, ProdutoList, ProdutoDetalhes, produto_json

# from .views import IndexView


urlpatterns = [
    # UPDATE -- OBTEM O ID ATRAVÉS DA URL
    path('editar/usuario/<int:pk>/',
         UsuarioUpdate.as_view(), name='editar-usuario'),
    path('editar/produto/<int:pk>', ProdutoUpdate.as_view(), name='editar-produto'),
    path('cadastrar/cor', CorCreate.as_view(), name='cadastrar-cor'),
    path('cadastrar/tamanho', TamanhoProdutoCreate.as_view(),
         name='cadastrar-tamanho'),
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    # DELETE -- OBTEM O ID ATRAVÉS DA URL
    path('excluir/usuario/<int:pk>/',
         UsuarioDelete.as_view(), name='excluir-usuario'),
    path('excluir/produto/<int:pk>',
         ProdutoDelete.as_view(), name='excluir-produto'),

    # LISTAR BANCO
    path('listar/usuarios/', UsuarioList.as_view(), name='listar-usuarios'),
    path('listar/produtos/', ProdutoList.as_view(), name='listar-produtos'),
    path('detalhes/produtos/<int:pk>/', ProdutoDetalhes, name='detalhar-produto'),
    path('produto/<int:pk>/json/', produto_json, name='produto_json'),
]
