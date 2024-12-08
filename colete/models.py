from django.db import models
from unidade.models import Unidade


class Colete(models.Model):
    modelo = models.CharField(max_length=20)
    tamanho = models.CharField(max_length=5)
    genero = models.CharField(max_length=20)
    numero_serie = models.IntegerField(null=True, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="Coletes")
    data_validade = models.DateField()
    data_fabricacao = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['modelo']
        
    def __str__(self):
        return self.modelo
    