from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Paciente, Clinica

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'ci', 'fecha_nacimiento', 'telefono', 'motivo_consulta', 'clinica']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Personalización de los claims del payload
        token['rol'] = getattr(user, 'rol', None)
        token['clinica_id'] = getattr(user, 'clinica_id', None)

        return token