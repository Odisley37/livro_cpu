from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def gerar_pdf(servico_data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    c.drawString(100, 750, f"Relatório de Serviço Diário")
    c.drawString(100, 730, f"Operador: {servico_data['operador']}")
    c.drawString(100, 710, f"Data: {servico_data['data']}")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer
