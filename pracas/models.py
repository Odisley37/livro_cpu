from django.db import models
from unidade.models import Unidade

class Praca(models.Model):
    name = models.CharField(max_length=100)
    name_war = models.CharField(max_length=20)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="pracas")
    graduacao = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)
    matricula = models.IntegerField()
    funcao = models.CharField(max_length=100, null=True, blank=True)
    sangue = models.CharField(max_length=2, null=True, blank=True)
    rh = models.CharField(max_length=1, null=True, blank=True)
    data_nascimento = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
