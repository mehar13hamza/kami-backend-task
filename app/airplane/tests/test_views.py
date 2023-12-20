from django.test import TestCase
from django.urls import reverse
import json
import random


class TestAirplaneView(TestCase):
    def test_create(self):
        response = self._create_records()
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        data = self._generate_data()
        records = self._create_records()
        record_id = records.data[0]['airplane_id']

        url = reverse('airplane-detail', kwargs={'airplane_id': record_id})
        response = self.client.get(url,  data=data)
        self.assertEqual(response.status_code, 200)

    def _generate_data(self):
        data = []
        passenger_count = random.randint(100, 10000)
        for i in range(10):
            data.append({'airplane_id': i+1, 'passengers': passenger_count})
        return data

    def _create_records(self):
        data = json.dumps(self._generate_data())
        url = reverse('airplane-list')
        response = self.client.post(url,  data=data, content_type='application/json')
        return response
   
