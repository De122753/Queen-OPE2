from django.db.models.fields import FloatField
from usuarios.models import Usuario
from django.db import models
from cadastros.models import Categoria, Produto
from .manager import EstoqueEntradaManager, EstoqueSaidaManager, EstoqueBaixaManager
from django.db.models import Sum


# Create your models here.


MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
    ('b', 'baixa'),
)

# classe para obter data e hora da criação e modificação


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now=False, auto_now_add=True)

    modified = models.DateTimeField(
        'modificado em', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(Usuario, verbose_name="Usuário", on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField(verbose_name='Nota Fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)
    nf_arquivo = models.FileField(upload_to='notas_fiscais/', verbose_name='NF. Arquivo', null=True, blank=True)

    # def clean(self):
    #     super(Estoque, self).clean()
    #     if self.movimento == 'b' and not self.nf and not self.nota_formatada and not self.nf_arquivo:
    #         raise ValidationError('Preenchimento obrigatório')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{}.{}.{}'.format(self.pk, self.nf, self.created.strftime('%d%m%Y'))
        return '{}.0000.{}'.format(self.pk, self.created.strftime('%d%m%Y'))

    def nota_formatada(self):
        if self.nf:
            return str(self.nf).zfill(6)
        return '000000'


class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


# cria tabela virtual somente com as saidas


class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saida'
        verbose_name_plural = 'estoque saida'


class EstoqueBaixa(Estoque):
    objects = EstoqueBaixaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque baixa'
        verbose_name_plural = 'estoque baixa'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, verbose_name='Produto: ', null=True)
    quantidade = models.PositiveIntegerField(verbose_name='Qtd.: ')
    saldo = models.PositiveIntegerField(verbose_name='Estoque: ')
    preco_unit = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, verbose_name='R$/Unid.')
    valor_item = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    fabricante = models.CharField(max_length=50, verbose_name='', blank=True, null=True)
    justificativa_baixa = models.CharField(verbose_name="", max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)

    # realiza o calcula do valor do item e atribui ao campo
    @property
    def calcula_total(self, *args, **kwargs):
        self.total = round(self.preco_unit * self.quantidade, 2)
        self.valor_item = self.total
        return super(EstoqueItens, self).save(*args, **kwargs)

    # Total geral
    @property
    def calcula_total_geral(self, *args, **kwargs):
        self.tt = EstoqueItens.objects.filter(estoque=self.estoque).values().aggregate(Sum('valor_item', output_field=FloatField()))
        self.tt = list(self.tt.values())[0]
        self.tt = round(self.tt, 2)
        return str(self.tt)
