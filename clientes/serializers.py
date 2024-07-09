from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self,data):
        if not cpf_valido(data['cpf']):
            raise  serializers.ValidationError({'cpf':"Cpf invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua numero nesse campo'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"o RG deve ter até 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"o Celular precisa o seguinte formato (11) 98604-9254"})
        return data

    