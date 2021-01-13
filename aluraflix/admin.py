from django.contrib import admin
from aluraflix.models import Programa

class Programas(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'data_lancamento', 'likes', 'dislikes']
    list_display_links = ['id', 'titulo']
    search_fields = ['titulo']
    list_filter = ['tipo']
    ordering = ['id']
    list_per_page = 10

admin.site.register(Programa, Programas)
