# Generated by Django 3.1.7 on 2021-05-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0023_estoque_nf_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf_arquivo',
            field=models.FileField(blank=True, null=True, upload_to='notas_fiscais/'),
        ),
    ]
