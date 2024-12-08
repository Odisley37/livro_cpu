from django.contrib import admin
from . import models

class OcorrenciasAdmin(admin.ModelAdmin):
    list_display = ('tipo',  )
    search_fields = ('tipo', )
    
admin.site.register(models.Ocorrencia, OcorrenciasAdmin)
