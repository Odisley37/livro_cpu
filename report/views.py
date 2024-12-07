# report/views.py
from django.http import HttpResponse
from .pdf_generator import gerar_pdf  # Importe a função de geração de PDF

def gerar_relatorio_pdf(request):
    # Dados de exemplo, você pode obter esses dados do banco de dados ou de um formulário
    servico_data = {
        'operador': 'Operador A',
        'data': '2024-12-07'
    }

    # Chama a função para gerar o PDF
    pdf = gerar_pdf(servico_data)

    # Configura a resposta HTTP para fornecer o PDF como download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatorio_servico.pdf"'

    return response
