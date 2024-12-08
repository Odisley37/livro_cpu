from django.contrib import admin
from . import models


class PracasAdmin(admin.ModelAdmin):
    list_display = ('name', 'graduacao', 'unidade', 'numero', 'name_war', )
    search_fields = ('name', )
    
admin.site.register(models.Praca, PracasAdmin)

