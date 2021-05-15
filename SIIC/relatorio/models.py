from django.db import models


class Report(models.Model):

    title = models.CharField('Título', max_length=100)
    date = models.DateField('Data', auto_now_add=True)
    description = models.TextField('Descrição')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Relatório'
        verbose_name_plural = 'Relatórios'
        ordering = ['-id']