from django import forms
from .models import Estoque, EstoqueItens, MOVIMENTO


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ('nf', 'nf_arquivo',)


class EstoqueIntensForm(forms.ModelForm):
    class Meta:
        model = EstoqueItens
        fields = ('produto', 'preco_unit',
                  'quantidade', 'saldo', 'fabricante',)
