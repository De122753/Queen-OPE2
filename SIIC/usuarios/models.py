# from SIIC.settings import TEMPLATES
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User, Group

# Create your models here.


################## CUSTOM USER MODEL ###########################
class Administrador(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError(
                'Forneça um nome de usuário válido para prosseguir')
        if not email:
            raise ValueError('Forneça um email válido para prosseguir')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome_completo = models.CharField(
        max_length=255, verbose_name='Nome completo')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    username = models.CharField(
        max_length=50, unique=True, verbose_name="Nome de usuário")
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    date_joined = models.DateTimeField(verbose_name="data de registro",
                                       auto_now=True)
    last_login = models.DateTimeField(
        verbose_name='ultimo login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = Administrador()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class meta:
        ordering = ('username',)
