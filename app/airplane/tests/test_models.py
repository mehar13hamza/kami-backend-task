from django.test import TestCase
from airplane.models import Airplane
from airplane.constants import BASE_FUEL_TANK_CAPACITY


class TestAirplane(TestCase):
    def setUp(self):
        self.airplane = Airplane(airplane_id=2, passengers=1000)

    def test_fuel_tank_capacity(self):
        expected_capacity = BASE_FUEL_TANK_CAPACITY * self.airplane.airplane_id
        self.assertEqual(self.airplane.fuel_tank_capacity, expected_capacity)

    def test_fuel_consumption_rate(self):
        self.assertEqual(self.airplane.fuel_consumption_rate, 2.55)

    def test_maximum_minutes_to_fly(self):
        self.assertEqual(self.airplane.maximum_minutes_to_fly, 156.59)
