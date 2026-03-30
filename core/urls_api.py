from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.api_views import PacienteListAPIView

urlpatterns = [
    # Endpoints para obtener y refrescar el Token JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoint para ver pacientes
    path('pacientes/', PacienteListAPIView.as_view(), name='api_pacientes_list'),
]