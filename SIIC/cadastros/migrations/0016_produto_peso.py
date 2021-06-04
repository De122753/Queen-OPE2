# Generated by Django 3.1.7 on 2021-05-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0015_auto_20210516_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Peso (Kg)'),
        ),
    ]