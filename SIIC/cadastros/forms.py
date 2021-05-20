from django import forms
from .models import Produto
from .models import Fornecedor, CorProduto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'


class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = '__all__'


class CorForm(forms.ModelForm):

    class Meta:
        model = CorProduto
        fields = ('cor_produto',)
