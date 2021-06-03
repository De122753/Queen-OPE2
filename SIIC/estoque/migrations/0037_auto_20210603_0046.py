# Generated by Django 3.1.7 on 2021-06-03 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0036_remove_estoqueitens_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota Fiscal *'),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='nf_arquivo',
            field=models.FileField(blank=True, null=True, upload_to='notas_fiscais/', verbose_name='NF. Arquivo *'),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='estoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.estoque', verbose_name='Item'),
        ),
    ]
