# Generated by Django 3.1.7 on 2021-05-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0028_auto_20210518_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf_arquivo',
            field=models.FileField(default=1, upload_to='notas_fiscais/'),
            preserve_default=False,
        ),
    ]
