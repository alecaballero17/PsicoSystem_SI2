from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # T011: Endpoints para obtener y refrescar el Token JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.api_views import PacienteListAPIView # Ahora vamos a crear esta vista

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # T014: Endpoint para ver pacientes desde la App Móvil/React
    path('pacientes/', PacienteListAPIView.as_view(), name='api_pacientes_list'),
]