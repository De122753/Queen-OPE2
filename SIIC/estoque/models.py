from usuarios.models import Usuario
from django.db import models
from django.contrib.auth.models import User
from cadastros.models import Produto
from django.urls.base import reverse_lazy
from django import forms

# Create your models here.

# classe para obter data e hora da criação e modificação

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now=False, auto_now_add=True)

    modified = models.DateTimeField(
        'modificado em', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(
        Usuario, verbose_name="Usuário", on_delete=models.CASCADE)
    nf = models.PositiveIntegerField(
        null=False, blank=False, verbose_name='Nota Fiscal')
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}.{}.{}'.format(self.pk, self.nf, self.created.strftime('%d%m%Y'))

    def nota_formatada(self):
        if self.nf:
            return str(self.nf).zfill(6)
        return '---'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)


# base para formulário para adicão de itens INLINE
