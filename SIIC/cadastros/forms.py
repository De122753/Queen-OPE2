from django import forms
from .models import Produto
from .models import Fornecedor


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'


class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = '__all__'
