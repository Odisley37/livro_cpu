from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from rest_framework import viewsets
from .models import ServicoInterno
from .forms import ServicoInternoForm, OcorrenciaForm
from .serializers import ServicoInternoSerializer


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
