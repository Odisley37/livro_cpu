from django.db import models
from unidade.models import Unidade

class Armamento(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    numero_serie = models.IntegerField()
    calibre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="armamentos")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['modelo']
        
    def __str__(self):
        return self.modelo
    