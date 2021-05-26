# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CadastrosCategoria(models.Model):
    categoria = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'cadastros_categoria'


class CadastrosCorproduto(models.Model):
    cor_produto = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'cadastros_corproduto'


class CadastrosProduto(models.Model):
    nome_produto = models.CharField(max_length=50)
    descricao_produto = models.CharField(max_length=255)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    quantidade_disponivel = models.PositiveIntegerField()
    cor_produto = models.ForeignKey(CadastrosCorproduto, models.DO_NOTHING)
    tamanho_produto = models.ForeignKey('CadastrosTamanhoproduto', models.DO_NOTHING)
    categoria = models.ForeignKey(CadastrosCategoria, models.DO_NOTHING, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadastros_produto'


class CadastrosTamanhoproduto(models.Model):
    tamanho_produto = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'cadastros_tamanhoproduto'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsuariosUsuario', models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstoqueEstoque(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    nf = models.PositiveIntegerField()
    movimento = models.CharField(max_length=1)
    funcionario = models.ForeignKey('UsuariosUsuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estoque_estoque'


class EstoqueEstoqueitens(models.Model):
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()
    estoque = models.ForeignKey(EstoqueEstoque, models.DO_NOTHING)
    valor_item = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    preco_unit = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    produto = models.ForeignKey(CadastrosProduto, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estoque_estoqueitens'


class UsuariosUsuario(models.Model):
    password = models.CharField(max_length=128)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=255)
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField()
    is_admin = models.BooleanField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    telefone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'usuarios_usuario'


class UsuariosUsuarioGroups(models.Model):
    usuario = models.ForeignKey(UsuariosUsuario, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuarios_usuario_groups'
        unique_together = (('usuario', 'group'),)


class UsuariosUsuarioUserPermissions(models.Model):
    usuario = models.ForeignKey(UsuariosUsuario, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuarios_usuario_user_permissions'
        unique_together = (('usuario', 'permission'),)
