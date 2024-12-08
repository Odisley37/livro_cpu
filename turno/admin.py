from django.contrib import admin
from . import models

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('turn', )
    search_fields = ('turn', )
    
admin.site.register(models.Turno, TurnosAdmin)