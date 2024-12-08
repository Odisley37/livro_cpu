from django.contrib import admin
from . import models

class ColetesAdmin(admin.ModelAdmin):
    list_display = ('modelo','data_fabricacao', 'data_validade', 'numero_serie', 'tamanho', 'genero',)
    search_fields = ('modelo', )
    
admin.site.register(models.Colete, ColetesAdmin)
