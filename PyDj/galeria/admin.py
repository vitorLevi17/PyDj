from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class ListFotografia(admin.ModelAdmin):
    list_display = ("id","nome","legenda")
    list_display_links = ("id","nome")
    search_fields = ("nome",)

admin.site.register(Fotografia,ListFotografia)

