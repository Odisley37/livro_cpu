from django.contrib import admin
from . import models

class TiposAdmin(admin.ModelAdmin):
    list_display = ('veiculo', )
    search_fields = ('veiculo', )
    
admin.site.register(models.Tipo, TiposAdmin)

# Register your models here.
