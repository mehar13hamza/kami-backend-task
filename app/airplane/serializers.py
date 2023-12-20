from rest_framework import serializers
from airplane.models import Airplane


class AirplaneListSerializer(serializers.ListSerializer):
    def validate(self, data):
        if len(data) != 10:
            raise serializers.ValidationError("Exactly 10 instances must be provided.")
        return data


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('airplane_id', 'passengers')
        list_serializer_class = AirplaneListSerializer

    def validate(self, data):
        if data['airplane_id']==0:
            raise serializers.ValidationError("Id must be a positive number.")
        return super().validate(data)


class AirplaneGetResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('fuel_consumption_rate', 'maximum_minutes_to_fly')
