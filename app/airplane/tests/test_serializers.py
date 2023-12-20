import random
from airplane.serializers import AirplaneSerializer
from django.test import TestCase
from rest_framework.exceptions import ValidationError


class TestAirplaneSerializer(TestCase):
    def test_airplane_serializer_validation_pass(self):
        data = self._generate_data()
        serializer = AirplaneSerializer(data=data, many=True)
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_airplane_serializer_validation_fails(self):
        data = self._generate_data()
        data.pop()
        serializer = AirplaneSerializer(data=data, many=True)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_airplane_serializer_doesnot_allow_id_to_be_zero(self):
        input_data = self._generate_data()
        input_data[0]['airplane_id'] = 0
        serializer = AirplaneSerializer(data=input_data, many=True)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def _generate_data(self):
        data = []
        passenger_count = random.randint(100, 10000)
        for i in range(10):
            data.append({'airplane_id': i+1, 'passengers': passenger_count})
        return data
