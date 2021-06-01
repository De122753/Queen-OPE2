"""
Django settings for SIIC project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n=4wn6bffd-ak+4^tv@^e30yo41su5+uoi6d3+7w*syqblo=s)'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Aplicações locais
    'paginas.apps.PaginasConfig',
    'cadastros.apps.CadastrosConfig',
    'usuarios.apps.UsuariosConfig',
    'estoque.apps.EstoqueConfig',
    'relatorio.apps.RelatorioConfig',

    'bootstrapform',
    'bootstrap4',
    'widget_tweaks',
    'crispy_forms',
    'bootstrap_modal_forms',
    'django_tables2',
    'django_filters',
    # nomedoapp.apps.Nomedoappconfig
]

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SIIC.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_USER_MODEL = 'usuarios.Usuario'
WSGI_APPLICATION = 'SIIC.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'TESTE',
#         'USER': 'queen',
#         'PASSWORD': '@@Que2021',
#         'HOST': 'serverqueen.database.windows.net',
#         'PORT': '1433',

#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEBUG = True

DECIMAL_SEPARATOR = ','

THOUSAND_SEPARATOR = '.'

USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#UPLOAD DE ARQUIVOS DE MIDIA
MEDIA_URL = "/uploads/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads')
# DATABASE_CONNECTION_POOLING = False


# CONFIGURAÇÕES DE AUTENTICAÇÃO

# Redireciona usuário para a página pós login
LOGIN_REDIRECT_URL = 'inicio'

# Redireciona usuário caso não tenha acesso à págiuna
LOGIN_URL = 'login'

# Redireciona usuário para a página pós logout
LOGOUT_REDIRECT_URL = 'login'
