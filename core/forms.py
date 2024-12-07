from django import forms
from .models import ServicoInterno, Escala, Ocorrencia, Viatura

class ServicoInternoForm(forms.ModelForm):
    class Meta:
        model = ServicoInterno
        fields = ['operador', 'horario_inicio', 'horario_fim', 'alteracao']
        widgets = {
            'operador': forms.TextInput(attrs={'class': 'form-control'}),
            'horario_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'horario_fim': forms.TextInput(attrs={'class': 'form-control'}),
            
            'alteracao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'operador': 'Operador',
            'horario_inicio': 'Início do serviço',
            'horario_fim': 'Fim do serviço',
            'alteracao': 'Alterações',
        }
class EscalaForm(forms.ModelForm):
    class Meta:
        model = Escala
        fields = ['operador', 'data', 'permuta', 'remanejamento']

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['operador', 'descricao', 'tipo']

class ViaturaForm(forms.ModelForm):
    class Meta:
        model = Viatura
        fields = ['modelo', 'placa', 'status']
