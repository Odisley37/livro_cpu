from django.urls import path
from . import views
from .views import ServicoInternoListView, listar_servicos

urlpatterns = [
    # Formulário de registro
    path('registrar_servico/', views.registrar_servico, name='registrar_servico'),
    path('registrar_ocorrencia/', views.registrar_ocorrencia, name='registrar_ocorrencia'),
    path('sucesso/', views.sucesso, name='sucesso'),
    
     path('servicos/', ServicoInternoListView.as_view(), name='servicointerno_list'),

    # CRUD para ServicoInterno
    path('servicos/', views.ServicoInternoListView.as_view(), name='servicointerno_list'),  # Listagem
    path('servicos/<int:pk>/', views.ServicoInternoDetailView.as_view(), name='servicointerno_detail'),  # Detalhes
    path('servicos/<int:pk>/editar/', views.ServicoInternoUpdateView.as_view(), name='servicointerno_update'),  # Edição
    path('servicos/<int:pk>/deletar/', views.ServicoInternoDeleteView.as_view(), name='servicointerno_delete'),  # Exclusão
]

