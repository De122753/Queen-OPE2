from django.db import models

from django.db import models

class TOTAL_PRODUTOS(models.Model):
    ID = models.PositiveIntegerField()
    CREATED = models.DateTimeField()
    NOME_PRODUTO = models.CharField(max_length=50)
    QUANTIDADE = models.PositiveIntegerField()
    MOVIMENTO = models.CharField(max_length=50)
    TOTAL = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'TOTAL_PRODUTOS'
"""
class TOTALIZADOR(models.Model):
    ID = models.PositiveIntegerField()
    MOVIMENTO = models.CharField(max_length=50)
    QUANTIDADE = models.PositiveIntegerField()
    TOTAL = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'TOTALIZADOR'
    

class RESULTADO_FINANC(models.Model):
    ID = models.PositiveIntegerField()
    RESULT = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'RESULTADO_FINANC'
"""
# class Report(models.Model):

#     title = models.CharField('Título', max_length=100)
#     date = models.DateField('Data', auto_now_add=True)
#     description = models.TextField('Descrição')

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = 'Relatório'
#         verbose_name_plural = 'Relatórios'
#         ordering = ['-id']


