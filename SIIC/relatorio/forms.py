from django import forms
from estoque.models import EstoqueItens

#class NameForm(forms.Form):
#    name = forms.CharField(label='Name', max_length=100, help_text='inserir nome', initial='Name')

class Relatorio(forms.ModelForm):
    class Meta:
        model = EstoqueItens
        fields = '__all__'

