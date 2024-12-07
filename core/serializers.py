from rest_framework import serializers
from core.models import ServicoInterno


class ServicoInternoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicoInterno
        fields = '__all__'