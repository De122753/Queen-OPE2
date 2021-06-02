from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import EstoqueItens, Estoque, EstoqueEntrada, EstoqueSaida

# Register your models here.

# inclusão linear de itens


class EstoqueItensInline(TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'funcionario', 'nf',
                    'movimento', 'funcionario',)
    search_fields = ('nf',)
    date_hierarchy = 'created'


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'funcionario', 'nf',
                    'movimento', 'funcionario',)
    search_fields = ('nf',)
    date_hierarchy = 'created'


@admin.register(EstoqueItens)
class EstoqueItensAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'estoque', 'produto', 'quantidade', 'saldo',)
    search_fields = ('produto',)
