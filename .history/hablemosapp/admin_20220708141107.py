import site
from django.contrib import admin
from .models import Debate, Comentario


class DebateAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'subtitulo', 'cuerpo', 'imagen')
    search_fields = ('titulo', 'subtitulo')

admin.site.register(Debate, DebateAdmin)


class ComentarioAdmin(admin.ModelAdmin):

    list_display = ('comentario', 'creado')
    
admin.site.register(Comentario, ComentarioAdmin)


# Register your models here.
