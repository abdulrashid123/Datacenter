from rest_framework import serializers
from table.models import Table, Parameter, Values


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'title')


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ('id', 'parameter_title')


class ValuesSerializer(serializers.ModelSerializer):
    parameter_name = serializers.CharField(read_only=True, source="Parameter.parameter_title")

    class Meta:
        model = Values

        fields = '__all__'




