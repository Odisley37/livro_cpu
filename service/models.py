from django.db import models

class Service(models.Model):
    user = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    date_service = models.DateTimeField()
    service_intern = models.TextField()
    quart_hour = models.TimeField()
    pm_permanence = models.CharField(max_length=100)
    permuts = models.CharField(max_length=100)
    remanejs = models.CharField(max_length=100)
    faltas = models.CharField(max_length=100)
    atrasos = models.CharField(max_length=100)
    baixas = models.CharField(max_length=100)
    lireracoes = models.CharField(max_length=100)
    viaturas = models.CharField(max_length=100)
    boletins = models.TextField()
    ocorrencia_transito = models.TextField()
    controle_tco = models.TextField()
    material_servico = models.TextField()
    ensino = models.TextField()
    instrucao = models.TextField()
    
    
