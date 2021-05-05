# Generated by Django 3.1.7 on 2021-05-01 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastros', '0006_auto_20210430_2135'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('nf', models.PositiveIntegerField(blank=True, null=True, verbose_name='Nota Fiscal')),
                ('movimento', models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], max_length=1)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='EstoquerItens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('saldo', models.PositiveIntegerField()),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.produto')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]