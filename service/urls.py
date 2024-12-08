from django.urls import path
from . import views  # Importe suas views corretamente

urlpatterns = [
    # Exemplo de uma URL
    path('service/', views.alguma_view, name='nome_da_rota'),
]
