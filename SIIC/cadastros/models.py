from django.db import models
from django.urls.base import reverse_lazy


class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(verbose_name='Nome do fornecedor', max_length=50)
    nome_fornecedor_redizido = models.CharField(verbose_name='Nome reduzido', max_length=50)
    cnpj_fornecedor = models.CharField(max_length=18, verbose_name='CNPJ')
    logradouro_fornecedor = models.CharField(verbose_name='Logradouro', max_length=50)
    numero_via_fornecedor = models.IntegerField(verbose_name='Número da via')
    cidade_fornecedor = models.CharField(verbose_name='Cidade', max_length=50)
    uf_fornecedor = models.CharField(verbose_name='UF', max_length=2)
    contato_fornecedor = models.CharField(verbose_name='Contato do fornecedor', max_length=255)
    email_fornecedor = models.EmailField(verbose_name='E-mail', max_length=254)
    telefone_fornecedor = models.CharField(max_length=15, verbose_name='Telefone')

    def __str__(self):
        return "{}".format(self.nome_fornecedor_redizido)

    def codigo_fornecedor_formatado(self):
        return str(self.pk).zfill(6)


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
    nome_produto = models.CharField(max_length=50, verbose_name='Nome do produto')
    descricao_produto = models.CharField(max_length=255, verbose_name='Descrição do produto', blank=True)
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço unitário')
    quantidade_disponivel = models.PositiveIntegerField(verbose_name='Quantidade disponível', default=0, null=True, blank=True)
    tamanho_produto = models.ForeignKey(TamanhoProduto, verbose_name="Tamanho", on_delete=models.CASCADE)
    cor_produto = models.ForeignKey(CorProduto, verbose_name="Cor do produto", on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=6, decimal_places=3, verbose_name='Peso (Kg)', blank=True, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    ncm = models.CharField(verbose_name='NCM', max_length=12)
    fabricante = models.ForeignKey('Fornecedor', verbose_name='Fornecedor', on_delete=models.CASCADE, null=True, blank=True)
    localizacao = models.CharField(verbose_name='Localização no Estoque', max_length=11)
    estoque_minimo = models.PositiveIntegerField(verbose_name='Estoque mínimo')
    foto = models.ImageField(null=True, blank=True, verbose_name="Foto do produto")

    def __str__(self):
        return "{} - {} | tam: {} | cor: {}".format(self.nome_produto, self.fabricante, self.tamanho_produto, self.cor_produto, )

    def get_absolute_url(self):
        return reverse_lazy("produto:detalhar-produto", kwargs={"pk": self.pk})
    # json

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.nome_produto,
            'estoque': self.quantidade_disponivel,
            'preco_unitario': self.preco_unitario,
            'fabricante': self.fabricante.nome_fornecedor_redizido
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
