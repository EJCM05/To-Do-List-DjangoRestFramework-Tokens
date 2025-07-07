from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User # Importa el modelo de usuario


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # Hace que 'owner' sea de solo lectura y muestre el nombre de usuario

    class Meta:
        model = Task
        fields = '__all__'