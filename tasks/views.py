from rest_framework import viewsets, permissions
from .models import *
from .serializers import TaskSerializer
from .permissions import *

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() # Eliminamos el .order_by aquí para poder usarlo con filtros/búsquedas más adelante
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # Primero autenticado, luego propietario

    def perform_create(self, serializer):
        """
        Asigna el propietario de la tarea al usuario que la está creando.
        """
        serializer.save(owner=self.request.user)