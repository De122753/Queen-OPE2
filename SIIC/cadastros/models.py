from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from usuarios.models import Usuario


# Create your models here.
# classe que define os atributos dos campos
# conforme o atributo da classe também valida os campos
# cada classe representa uma tabela na base de dados


class StatusPedido(models.Model):
    status_pedido = models.CharField(
        max_length=50, verbose_name='Status do pedidos', unique=True)

    def __str__(self):
        return "{}".format(self.status_pedido)


class TipoMovimentacao(models.Model):
    tipo_movimentacao = models.CharField(
        max_length=50, verbose_name="Tipo de movimentação", unique=True)

    def __str__(self):
        return "{}".format(self.tipo_movimentacao)


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


class Pedido(models.Model):
    valor_pedido = models.DecimalField(
        decimal_places=2, max_digits=6, verbose_name="Valor do pedido"
    )
    data_pedido = models.DateField(
        auto_now=True, verbose_name='Data da abertura')
    data_fechamento = models.DateField(
        verbose_name='Data do fechamento', blank=True)
    frete = models.DecimalField(
        decimal_places=2, max_digits=2, verbose_name='Valor do frete')
    nota_fiscal = models.IntegerField(verbose_name='Numero da nota fiscal')
    pedido_ususario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    status_pedido = models.ForeignKey(
        StatusPedido, on_delete=models.PROTECT, verbose_name='Status')
    tipo_movimentacao = models.ForeignKey(
        TipoMovimentacao, on_delete=models.PROTECT, verbose_name='Movimentação')

    # chave estrangeira protegida quando há dependências
    # usuario_pedido = models.ForeignKey(
    #      Usuario, on_delete=models.PROTECT)

    # metodo para pegar o valor do campo e imprimir na tela

    def __str__(self):
        return "Usuário: {}".format(self.pedido_usuario)


class Produto(models.Model):
    nome_produto = models.CharField(
        max_length=50, verbose_name='Nome do produto')
    descricao_produto = models.CharField(
        max_length=255, verbose_name='Descrição do produto', blank=True)
    preco_unitario = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name='Preço unitário')
    quantidade_disponivel = models.PositiveIntegerField(
        verbose_name='Quantidade disponíve')
    tamanho_produto = models.ForeignKey(
        TamanhoProduto, verbose_name="Tamanho do produto", on_delete=models.CASCADE)
    cor_produto = models.ForeignKey(
        CorProduto, verbose_name="Cor do produto", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome_produto)

    def get_absolute_url(self):
        return reverse_lazy("produto:detalhar-produto", kwargs={"pk": self.pk})


class Item(models.Model):
    quantidade_item = models.IntegerField(
        verbose_name="Quantidade de produtos")
    desconto = models.DecimalField(
        max_digits=5, decimal_places=4, verbose_name='Desconto', blank=True)
    valor_item = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Valor do item')
    produto = models.ForeignKey(
        Produto, verbose_name='Produto', on_delete=models.CASCADE)
    pedido = models.ForeignKey(
        Pedido, verbose_name='Pedido N.', on_delete=models.CASCADE)
