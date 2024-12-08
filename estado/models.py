from django.db import models
from unidade.models import Unidade


class Estado(models.Model):
    tipo = models.CharField(max_length=20)    
    
    class Meta:
        ordering = ['tipo']
        
    def __str__(self):
        return self.tipo
    
