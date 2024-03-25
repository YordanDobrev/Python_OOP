from unittest import TestCase, main

#from forth_car_manager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Reno", "Megan", 15, 75)

    def test_correct_init(self):
        self.assertEqual("Reno", self.car.make)
        self.assertEqual("Megan", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_is_not_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_is_not_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_is_not_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_not_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_is_not_less_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_is_not_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_successful_refuel_the_tank(self):
        expected_result = self.car.refuel(10)

        self.car.refuel(10)

        self.assertEqual(expected_result, self.car.refuel(10))

    def test_driving_the_car_with_given_distance(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(73.5, self.car.fuel_amount)

    def test_if_the_needed_fuel_is_enough(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1100000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
