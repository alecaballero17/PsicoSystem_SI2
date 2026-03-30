from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Paciente
from .serializers import PacienteSerializer, MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    # Usa nuestro serializador personalizado en lugar del que viene por defecto
    serializer_class = MyTokenObtainPairSerializer


class PacienteListAPIView(APIView):
    # Solo usuarios con Token JWT válido pueden entrar
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Lógica Multi-tenant: Filtramos pacientes por la clínica del usuario logueado
        pacientes = Paciente.objects.filter(clinica=request.user.clinica)
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)