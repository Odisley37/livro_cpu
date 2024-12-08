from django.db import models

class Unidade(models.Model):
    unidade = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['unidade']
        
    def __str__(self):
        return self.unidade
    
