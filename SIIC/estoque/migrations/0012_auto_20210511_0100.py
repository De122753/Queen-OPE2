# Generated by Django 3.1.7 on 2021-05-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0011_estoqueitens_valor_item_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoqueitens',
            name='valor_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='valor_item_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]