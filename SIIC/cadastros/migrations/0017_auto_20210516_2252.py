# Generated by Django 3.1.7 on 2021-05-17 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0016_produto_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Peso (Kg)'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tamanho_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.tamanhoproduto', verbose_name='Tamanho'),
        ),
    ]