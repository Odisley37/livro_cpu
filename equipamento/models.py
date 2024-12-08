from django.db import models
from unidade.models import Unidade


class Equipamento(models.Model):
    tipo = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    numero_serie = models.IntegerField(null=True, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="equipamentos")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['tipo']
        
    def __str__(self):
        return self.tipo
    