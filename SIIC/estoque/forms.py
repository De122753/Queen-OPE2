from django import forms
from .models import Estoque, EstoqueItens


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ('nf',)


class EstoqueIntensForm(forms.ModelForm):
    class Meta:
        model = EstoqueItens
        fields = ('produto', 'quantidade', 'saldo',
                  'preco_unit',)  # '__all__'
