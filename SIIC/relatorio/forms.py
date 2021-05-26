from django import forms
from estoque.models import Estoque
from relatorio.models import TOTAL_PRODUTOS, TOTALIZADOR

#class NameForm(forms.Form):
#    name = forms.CharField(label='Name', max_length=100, help_text='inserir nome', initial='Name')

# class Relatorio(forms.ModelForm):
#     class Meta:
#         model = TOTAL_PRODUTOS
#         fields = '__all__'

# class Relatorio_Total(forms.ModelForm):
#     class Meta:
#         model = TOTALIZADOR
#         fields = '__all__'