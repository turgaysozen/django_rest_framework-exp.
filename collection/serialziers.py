from rest_framework import serializers
from .models import Operation, Bin


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = '__all__'
