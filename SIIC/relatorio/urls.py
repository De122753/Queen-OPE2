from django.urls import path
from .views import relatorio_movimento

urlpatterns = [
    path('relatorio/', relatorio_movimento, name='relatorio_movimento'),
]