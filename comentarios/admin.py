from django.contrib import admin
from .models import Comentario
from .actions import reprova_comentarios, aprova_comentarios


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'comentario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]