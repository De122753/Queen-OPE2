from django.urls import path
from .views import relatorio_movimento, HelloPDFView
from . import views
from django.conf.urls import url



urlpatterns = [
    path('relatorio/', relatorio_movimento, name='relatorio_movimento'),
    url('', HelloPDFView.as_view(), name='templatepdf'),
]