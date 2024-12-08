from django.contrib import admin
from . import models

class UnidadesAdmin(admin.ModelAdmin):
    list_display = ('unidade', 'city', 'tipo',  )
    search_fields = ('unidade', )
    
admin.site.register(models.Unidade, UnidadesAdmin)
