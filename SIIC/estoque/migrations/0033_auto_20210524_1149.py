# Generated by Django 3.1.7 on 2021-05-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0032_auto_20210524_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf',
            field=models.PositiveIntegerField(blank=True, default='0', null=True, verbose_name='Nota Fiscal'),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='nf_arquivo',
            field=models.FileField(blank=True, null=True, upload_to='notas_fiscais/', verbose_name='NF. Arquivo'),
        ),
    ]
