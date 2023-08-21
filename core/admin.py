from django.contrib import admin
from .models import PontoTuristico, DocIdentificacao


@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'aprovado']

admin.site.register(DocIdentificacao)
