import django_filters
from .models import Estoque, EstoqueItens, DetailedDataTable, TimeStampedModel


class ItensFilter(django_filters.FilterSet):
    class Meta:
        model = Estoque
        fields = ('movimento',)
