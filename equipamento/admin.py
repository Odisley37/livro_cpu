from django.contrib import admin
from . import models

class EquipamentosAdmin(admin.ModelAdmin):
    list_display = ('modelo','tipo', 'numero_serie',  )
    search_fields = ('modelo', )
    
admin.site.register(models.Equipamento, EquipamentosAdmin)