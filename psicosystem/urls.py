from django.contrib import admin
from django.urls import path
from core.views import registrar_clinica_view, registrar_usuario_view # Importa la nueva vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro-clinica/', registrar_clinica_view, name='registrar_clinica'),
    # Nueva ruta CU02
    path('registro-psicologo/', registrar_usuario_view, name='registrar_psicologo'),
]