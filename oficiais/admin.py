from django.contrib import admin
from . import models

class OficiaisAdmin(admin.ModelAdmin):
    list_display = ('name', 'quadro', 'posto', 'unidade', 'funcao', 'name_war', )
    search_fields = ('name', )
    
admin.site.register(models.Oficial, OficiaisAdmin)

# Register your models here.
