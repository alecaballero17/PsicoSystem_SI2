from django.contrib import admin
from django.urls import path, include  # <-- IMPORTANTE: Añadimos 'include'
from core.views import registrar_clinica_view, registrar_usuario_view, registrar_paciente_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- RUTAS DE LA WEB (Templates/HTML) ---
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('registro-clinica/', registrar_clinica_view, name='registrar_clinica'),
    path('registro-psicologo/', registrar_usuario_view, name='registrar_psicologo'),
    path('registro-paciente/', registrar_paciente_view, name='registrar_paciente'),

    # --- RUTAS DE LA API (Para el Auditor/Móvil/React) ---
    # Esto busca el archivo core/urls_api.py que creamos antes
    path('api/', include('core.urls_api')),
]