from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relatorio/', include('report.urls')), 
    path('core/', include('core.urls')),  
    
    path('service/', include('service.urls')), 
    
]
