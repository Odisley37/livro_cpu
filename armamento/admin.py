from django.contrib import admin
from . import models

class ArmamentosAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'calibre', 'marca', 'unidade',  )
    search_fields = ('modelo', )
    
admin.site.register(models.Armamento, ArmamentosAdmin)