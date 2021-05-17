from functools import total_ordering
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.urls.base import reverse_lazy
from usuarios.models import Usuario


# Create your models here.
# classe que define os atributos dos campos
# conforme o atributo da classe também valida os campos
# cada classe representa uma tabela na base de dados


class CorProduto(models.Model):
    cor_produto = models.CharField(
        max_length=50, verbose_name='Cor do produto', unique=True)

    class Meta:
        ordering = ['cor_produto']

    def __str__(self):
        return "{}".format(self.cor_produto)


class TamanhoProduto(models.Model):
    tamanho_produto = models.CharField(
        max_length=50, verbose_name='Tamanho do produto', unique=True)

    def __str__(self):
        return "{}".format(self.tamanho_produto)


class Produto(models.Model):
    nome_produto = models.CharField(
        max_length=50, verbose_name='Nome do produto')
    descricao_produto = models.CharField(
        max_length=255, verbose_name='Descrição do produto', blank=True)
    preco_unitario = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Preço unitário', blank=True, null=True)
    quantidade_disponivel = models.PositiveIntegerField(
        verbose_name='Quantidade disponíve')
    tamanho_produto = models.ForeignKey(
        TamanhoProduto, verbose_name="Tamanho", on_delete=models.CASCADE)
    cor_produto = models.ForeignKey(
        CorProduto, verbose_name="Cor do produto", on_delete=models.CASCADE)
    peso = models.DecimalField(
        max_digits=6, decimal_places=3, verbose_name='Peso (Kg)', blank=True, null=True)
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    ncm = models.CharField(verbose_name='NCM', max_length=10)
    fabricante = models.CharField(
        verbose_name='Fabricante/Fornecedor', max_length=50)
    localizacao = models.CharField(
        verbose_name='Localização no Estoque', max_length=11)
    estoque_minimo = models.PositiveIntegerField(verbose_name='Estoque mínimo')
    foto = models.ImageField(null=True, blank=True,
                             verbose_name="Foto do produto")

    def __str__(self):
        return "{} | tam: {} | cor: {}".format(self.nome_produto, self.tamanho_produto, self.cor_produto)

    def get_absolute_url(self):
        return reverse_lazy("produto:detalhar-produto", kwargs={"pk": self.pk})
    # json

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.nome_produto,
            'estoque': self.quantidade_disponivel,
            'preco_unitario': self.preco_unitario,
        }

    def codigo_produto_formatado(self):
        return str(self.pk).zfill(6)


class Categoria(models.Model):
    categoria = models.CharField(
        max_length=50, unique=True, verbose_name='Categoria')

    class Meta:
        ordering = ('categoria',)

    def __str__(self):
        return self.categoria
