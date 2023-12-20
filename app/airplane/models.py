import math
from django.db import models
from airplane.constants import (
    BASE_FUEL_TANK_CAPACITY,
    BASE_FUEL_CONSUMPTION_MUTLIPLIER,
    PASSENGER_FUEL_CONSUMPTION_RATE,
)


class Airplane(models.Model):

    airplane_id = models.IntegerField(primary_key=True, unique=True)
    passengers = models.PositiveIntegerField("number of passengers")

    @property
    def maximum_minutes_to_fly(self) -> float:
        """
        Calculates the maximum minutes the airplane can fly based on its fuel consumption rate.

        Returns:
        - float: The maximum minutes the airplane can fly.
        """
        final_rate = self.get_fuel_consumption_rate()
        fuel_tank_capacity = self.get_fuel_tank_capacity()
        return round(fuel_tank_capacity / final_rate, 2)

    def get_fuel_tank_capacity(self) -> int:
        """
        Calculates the fuel tank capacity based on the airplane ID.

        Returns:
        - int: The fuel tank capacity.
        """
        return BASE_FUEL_TANK_CAPACITY * self.airplane_id

    @property
    def fuel_tank_capacity(self) -> int:
        return self.get_fuel_tank_capacity()

    def get_fuel_consumption_rate(self) -> float:
        """
        Calculates the fuel consumption rate based on the airplane ID and number of passengers.

        Returns:
        - float: The fuel consumption rate.
        """
    
        base_fuel_consumption_rate = (
            math.log(self.airplane_id) * BASE_FUEL_CONSUMPTION_MUTLIPLIER
        )
        fuel_consumption_rate_with_passengers = (
            self.passengers * PASSENGER_FUEL_CONSUMPTION_RATE
        )
        return base_fuel_consumption_rate + fuel_consumption_rate_with_passengers

    @property
    def fuel_consumption_rate(self) -> float:
        """
        Returns the fuel consumption rate of the airplane.

        Returns:
        - float: The fuel consumption rate.
        """
        return round(self.get_fuel_consumption_rate(), 2)
