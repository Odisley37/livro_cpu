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
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from datetime import date
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from io import BytesIO


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
    servicointerno = get_object_or_404(ServicoInterno, id=id)
    
    # Configura o HttpResponse para download do PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="livro_cpu_{id}.pdf"'

    # Configuração do PDF
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4
    margin = 50  # Margem
    available_width = width - (2 * margin)  # Largura disponível para o conteúdo
    y_position = height - margin  # Posição inicial

    def verifica_pagina():
        """Verifica se é necessário criar uma nova página."""
        nonlocal y_position
        if y_position < margin + 100:
            p.showPage()  # Gera uma nova página
            y_position = height - margin  # Reinicia a posição no topo da nova página

    def desenha_cabecalho():
        """Desenha o cabeçalho com as imagens e texto."""
        nonlocal y_position
        image_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')  # Ajuste o caminho
        img_left = os.path.join(image_dir, 'brasao1.png')
        img_center = os.path.join(image_dir, 'brasao2.png')
        img_right = os.path.join(image_dir, 'brasao3.png')

        if os.path.exists(img_left):
            p.drawImage(img_left, margin, y_position - 50, width=50, height=50, mask='auto')
        if os.path.exists(img_center):
            p.drawImage(img_center, (width / 2) - 25, y_position - 50, width=50, height=50, mask='auto')
        if os.path.exists(img_right):
            p.drawImage(img_right, width - margin - 50, y_position - 50, width=50, height=50, mask='auto')

        y_position -= 70
        p.setFont("Times-Roman", 12)
        header_text = [
            "ESTADO DO MARANHÃO",
            "SECRETARIA DE SEGURANÇA PÚBLICA",
            "POLÍCIA MILITAR",
            "COMANDO DE POLICIAMENTO DO INTERIOR",
            "COMANDO DE ÁREA 4",
            "11º BATALHÃO DE POLÍCIA MILITAR"
        ]
        for line in header_text:
            p.drawCentredString(width / 2, y_position, line)
            y_position -= 15
        p.line(margin, y_position, width - margin, y_position)
        y_position -= 30

    def desenha_secao(texto):
        """Desenha a seção com o título destacado."""
        nonlocal y_position
        p.setFont("Times-Bold", 13)
        p.setFillColor(colors.grey)
        p.rect(margin, y_position - 25, available_width, 30, fill=True, stroke=False)
        p.setFillColor(colors.white)
        p.drawCentredString(width / 2, y_position, texto.upper())
        y_position -= 50
        verifica_pagina()

    def desenha_tabela(headers, rows):
        """Desenha uma tabela com dados ajustados à largura disponível."""
        nonlocal y_position
        col_widths = [available_width / len(headers)] * len(headers)
        data = [headers] + rows
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('FONTNAME', (0, 0), (-1, -1), 'Times-Roman'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ]))
        table_height = len(data) * 20
        verifica_pagina()
        table.wrapOn(p, margin, y_position)
        table.drawOn(p, margin, y_position - table_height)
        y_position -= table_height + 20

    # Cabeçalho
    desenha_cabecalho()

    # Primeira Parte
    desenha_secao("Primeira Parte - Serviço Diário")
    p.setFont("Times-Bold", 12)
    p.drawString(margin, y_position, "1.1. Serviço Interno")
    y_position -= 20

    p.setFont("Times-Roman", 10)
    p.drawString(margin + 20, y_position, "a. Permanência")
    y_position -= 20
    permanencia_rows = [
        ["11 BPM", "", ""],
        ["47 BPM", "", ""],
    ]
    desenha_tabela(["Unidade", "Quarto de Hora", "PM"], permanencia_rows)

    p.drawString(margin + 20, y_position, "b. Alterações do Serviço Interno")
    y_position -= 20
    alteracoes_rows = [["", "", "", "", "", ""] for _ in range(3)]
    desenha_tabela(["Desp. SubCMT", "OPM", "PM", "Posto Escalado", "Turno/Hora", "Observações"], alteracoes_rows)

    # Segunda Parte
    desenha_secao("Segunda Parte - Ensino e Instrução")
    # Adicionar conteúdo conforme necessário

    # Finaliza o documento
    p.showPage()
    p.save()
    return response