from rest_framework import serializers
from .models import Registro


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['peso','fecha','created_at']

    def validate_peso(self,value):
        """ 
        Check if field peso is positive
        """
        if value < 0:
            raise serializers.ValidationError('Peso no puede ser negativo')
        return value
