from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 150)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_fuel_is_not_enough_raise_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_decreasing_fuel(self):
        result = self.vehicle.fuel - (self.vehicle.DEFAULT_FUEL_CONSUMPTION * 10)

        self.vehicle.drive(10)

        self.assertEqual(result, self.vehicle.fuel)

    def test_more_than_tank_capacity_is_refueled_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_tank_refueling(self):
        self.vehicle.fuel = 0

        self.vehicle.refuel(20)

        self.assertEqual(20, self.vehicle.fuel)

    def test_the__str__method(self):
        self.assertEqual(f"The vehicle has 150 " \
                         f"horse power with 100 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())


if __name__ == "__main__":
    main()
