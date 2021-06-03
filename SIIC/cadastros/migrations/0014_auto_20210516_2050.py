# Generated by Django 3.1.7 on 2021-05-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_auto_20210515_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estoque_minimo',
            field=models.PositiveIntegerField(default=1, verbose_name='Estoque mínimo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='fabricante',
            field=models.CharField(default=1, max_length=50, verbose_name='Fabricante/Fornecedor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='localizacao',
            field=models.CharField(default=1, max_length=50, verbose_name='Localização no Estoque'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='ncm',
            field=models.CharField(default=1, max_length=50, verbose_name='NCM'),
            preserve_default=False,
        ),
    ]
