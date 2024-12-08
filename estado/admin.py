from django.contrib import admin
from . import models

class EstadosAdmin(admin.ModelAdmin):
    list_display = ('tipo',  )
    search_fields = ('tipo', )
    
admin.site.register(models.Estado, EstadosAdmin)