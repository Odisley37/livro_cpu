from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework import viewsets
from .models import ServicoInterno
from .forms import ServicoInternoForm, OcorrenciaForm
from .serializers import ServicoInternoSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import ServicoInterno
from reportlab.pdfgen import canvas



# API ViewSet para ServicoInterno
class ServicoInternoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para API REST de ServicoInterno.
    Permite criar, listar, atualizar e deletar.
    """
    queryset = ServicoInterno.objects.all()
    serializer_class = ServicoInternoSerializer


# Listagem de Serviços Internos
class ServicoInternoListView(ListView):
    """
    Exibe a lista de todos os serviços internos cadastrados.
    """
    model = ServicoInterno
    template_name = 'core/servico_list.html'
    context_object_name = 'servicointernos'


# Detalhes de um Serviço Interno
class ServicoInternoDetailView(DetailView):
    """
    Exibe os detalhes de um serviço interno específico.
    """
    model = ServicoInterno
    template_name = 'core/servico_detail.html'
    context_object_name = 'servicointerno'


# Criação de um novo Serviço Interno
class ServicoInternoCreateView(CreateView):
    """
    Formulário para criar um novo serviço interno.
    """
    model = ServicoInterno
    form_class = ServicoInternoForm
    template_name = 'core/servico_form.html'
    success_url = reverse_lazy('servicointerno_list')

class ServicoListView(ListView):
    model = ServicoInterno
    template_name = 'servico_list.html'
    context_object_name = 'servicos'

# Atualização de um Serviço Interno
class ServicoInternoUpdateView(UpdateView):
    """
    Formulário para editar um serviço interno existente.
    """
    model = ServicoInterno
    form_class = ServicoInternoForm
    template_name = 'core/servico_form.html'
    success_url = reverse_lazy('servicointerno_list')


# Exclusão de um Serviço Interno
class ServicoInternoDeleteView(DeleteView):
    """
    Página para confirmar a exclusão de um serviço interno.
    """
    model = ServicoInterno
    template_name = 'core/servico_confirm_delete.html'
    success_url = reverse_lazy('servicointerno_list')


# Função para registrar um serviço interno (manual)
def registrar_servico(request):
    """
    Renderiza e processa o formulário de registro de serviço interno.
    """
    if request.method == 'POST':
        form = ServicoInternoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = ServicoInternoForm()

    return render(request, 'core/registrar_servico.html', {'form': form})


# Função para registrar uma ocorrência
def registrar_ocorrencia(request):
    """
    Renderiza e processa o formulário de registro de ocorrência.
    """
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = OcorrenciaForm()

    return render(request, 'core/registrar_ocorrencia.html', {'form': form})


# Página de sucesso
def sucesso(request):
    """
    Exibe uma página de sucesso após a conclusão de uma ação.
    """
    return render(request, 'core/sucesso.html')

def listar_servicos(request):
    """
    Lista os serviços internos cadastrados.
    """
    servicointernos = ServicoInterno.objects.all()
    return render(request, 'core/registrar_servico.html', {'servicointernos': servicointernos})


def gerar_relatorio_pdf(request, id):
    servicointerno = get_object_or_404(ServicoInterno, id=id)  # Carrega o objeto ou retorna 404
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="relatorio_servico_{id}.pdf"'

    # Gerando o PDF
    p = canvas.Canvas(response)
    p.drawString(100, 800, "Relatório de Serviço Interno")
    p.drawString(100, 750, f"Operador: {servicointerno.operador}")  # Atualize para o campo correto
    p.drawString(100, 730, f"inicio do Serviço: {servicointerno.horario_inicio}")
    p.drawString(100, 710, f"Fim do Serviço: {servicointerno.horario_fim}")
    p.drawString(100, 690, f"Alteração: {servicointerno.alteracao}")

    p.showPage()
    p.save()
    return response