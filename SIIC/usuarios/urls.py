from django.urls import path
# MÓDUDO PARA AUTENTICAÇÃO DE USUÁRIOS
# (passar um alias para não conflitar com a views da aplicação)
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, alterar_senha

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
    path('alterar-senha/', alterar_senha, name='alterar-senha'),
]
