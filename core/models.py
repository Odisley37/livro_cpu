from django.db import models

class ServicoInterno(models.Model):
    operador = models.CharField(max_length=100)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    alteracao = models.TextField(blank=True)

class Escala(models.Model):
    operador = models.ForeignKey('ServicoInterno', on_delete=models.CASCADE)
    data = models.DateField()
    permuta = models.BooleanField(default=False)
    remanejamento = models.BooleanField(default=False)

class Ocorrencia(models.Model):
    operador = models.ForeignKey('ServicoInterno', on_delete=models.CASCADE)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50)
    data_ocorrencia = models.DateTimeField(auto_now_add=True)

class Viatura(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    status = models.CharField(max_length=20)  # Disponível, Em serviço, etc.
