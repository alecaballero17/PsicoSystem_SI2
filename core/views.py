from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# IMPORTACIÓN DE MODELOS (Esto corrige el NameError)
from .models import Clinica, Usuario, Paciente 

# IMPORTACIÓN DE FORMULARIOS
from .forms import ClinicaForm, RegistroUsuarioForm, PacienteForm

# --- CASOS DE USO ---

def is_admin(user):
    return user.is_authenticated and (getattr(user, 'rol', None) == 'ADMIN' or user.is_superuser)

def admin_required(view_func):
    """
    T018: Decorador para verificar si el usuario tiene rol de ADMIN.
    Redirige al dashboard si no tiene permisos.
    """
    return user_passes_test(is_admin, login_url='dashboard')(view_func)

@login_required 
def dashboard_view(request):
    """
    CU03: Dashboard para Psicólogos.
    Muestra la lista de pacientes filtrada por la clínica del usuario logueado.
    """
    pacientes = Paciente.objects.filter(clinica=request.user.clinica)
    return render(request, 'core/dashboard.html', {'pacientes': pacientes})

@login_required
@admin_required
def registrar_clinica_view(request):
    """
    CU25: Registro de Clínicas (SaaS Tenant).
    """
    if request.method == 'POST':
        form = ClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard') # Redirigimos al dashboard ahora que existe
    else:
        form = ClinicaForm()
    return render(request, 'core/registrar_clinica.html', {'form': form})

@login_required
@admin_required
def registrar_usuario_view(request):
    """
    CU02: Registro de Psicólogos.
    """
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'core/registrar_usuario.html', {'form': form})

@login_required
def registrar_paciente_view(request):
    """
    CU06: Registro de Pacientes con lógica Multi-tenant.
    """
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            # ASIGNACIÓN AUTOMÁTICA de la clínica para aislamiento de datos
            paciente.clinica = request.user.clinica 
            paciente.save()
            return redirect('dashboard')
    else:
        form = PacienteForm()
    return render(request, 'core/registrar_paciente.html', {'form': form})