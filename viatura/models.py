from django.db import models
from tipo.models import Tipo
from unidade.models import Unidade

class Veiculo(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name="veiculos")
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="veiculos")
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.DateField()
    placa = models.CharField(max_length=10)
    prefixo = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['tipo']
        
    def __str__(self):
        return self.tipo
