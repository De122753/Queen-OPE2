from django import forms
from .models import Estoque, EstoqueItens
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ('nf', 'nf_arquivo',)


class EstoqueIntensForm(forms.ModelForm):
    class Meta:
        model = EstoqueItens
        fields = ('produto', 'preco_unit', 'quantidade', 'saldo', 'fabricante'
                  )  # '__all__'

    # # personalização do crispy form

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
