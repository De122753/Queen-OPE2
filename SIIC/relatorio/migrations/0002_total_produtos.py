# Generated by Django 3.1.7 on 2021-06-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOTAL_PRODUTOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.PositiveIntegerField()),
                ('CREATED', models.DateTimeField()),
                ('NOME_PRODUTO', models.CharField(max_length=50)),
                ('QUANTIDADE', models.PositiveIntegerField()),
                ('MOVIMENTO', models.CharField(max_length=50)),
                ('TOTAL', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'TOTAL_PRODUTOS',
                'managed': False,
            },
        ),
    ]