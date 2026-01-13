from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas da API (Alunos, Turmas, etc)
    path('api/', include('core.urls')), 
    
    # Rotas de Autenticação (Login) - O ERRO ESTÁ AQUI SE FALTAR ISSO
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]