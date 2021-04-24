# from SIIC.usuarios.models import Usuario
from django.contrib import admin
from .models import Usuario

# Register your models here.


@admin.register(Usuario)
# admin.site.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'username',
        'nome_completo',
        'email',
        'date_joined'
    )
    search_fields = ('username',)
    list_filter = ('username',)
