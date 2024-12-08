from django.contrib import admin
from . import models

class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('modelo','prefixo', 'placa',  )
    search_fields = ('modelo', )
    
admin.site.register(models.Veiculo, VeiculosAdmin)