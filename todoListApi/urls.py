# todo_api_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tasks.views import *
from rest_framework.authtoken.views import obtain_auth_token # Importa la vista para obtener token
from django.contrib.auth.models import User # Importa el modelo de usuario
from rest_framework import generics, serializers

# Serializador simple para el registro de usuarios
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Vista para el registro de usuarios
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,) # Permite a cualquiera registrarse

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Para la interfaz de inicio de sesión de DRF
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'), # Endpoint para obtener el token
    path('api/register/', UserCreate.as_view(), name='register'), # Endpoint para registrar usuarios
]