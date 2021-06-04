from django.urls import path
from .views import relatorio_movimento
from . import views


urlpatterns = [
    path('relatorio/', relatorio_movimento, name='relatorio_movimento'),  

]