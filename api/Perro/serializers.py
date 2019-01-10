# from paradigma.serializers.model_serializers import DynamicFieldsModelSerializer, RecursiveField
from .models import Perro
from rest_framework import serializers

class PerroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perro
        fields = ('id', 'nombre', 'apellido', 'raza', 'edad')

