# Generated by Django 3.1.7 on 2021-05-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0027_estoqueitens_fabricante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='fabricante',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=''),
        ),
    ]