# report/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('gerar-pdf/', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
]

