# Generated by Django 3.1.7 on 2021-06-01 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0035_estoqueitens_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoqueitens',
            name='created',
        ),
    ]
