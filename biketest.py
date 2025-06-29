import unittest
from bike import Bike


class BikeTest(unittest.TestCase):

    def setUp(self):
        self.my_bike = Bike()

    def test_bike_can_be_turned_on(self):
        self.assertFalse(self.my_bike.check_bike_is_on())

        self.my_bike.toggle_power()
        self.assertTrue(self.my_bike.check_bike_is_on())

    def test_bike_can_be_turned_off(self):
        self.assertFalse(self.my_bike.check_bike_is_on())
        self.my_bike.toggle_power()
        self.assertTrue(self.my_bike.check_bike_is_on())

        self.my_bike.toggle_power()
        self.assertFalse(self.my_bike.check_bike_is_on())

    def test_bike_can_be_accelerated(self):
        self.assertFalse(self.my_bike.check_bike_is_on())
        self.my_bike.toggle_power()
        self.assertTrue(self.my_bike.check_bike_is_on())
        self.assertEqual(self.my_bike.get_current_speed(), 0)

        gear = 1
        for number in range(21): self.my_bike.accelerate(gear)

        self.assertEqual(self.my_bike.get_current_speed(), 21)

        gear = 2
        for number in range(5): self.my_bike.accelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 31)

        gear = 3
        for number in range(4): self.my_bike.accelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 43)

        gear = 4
        for number in range(5): self.my_bike.accelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 63)

    def test_bike_can_be_decelerated(self):
        self.assertFalse(self.my_bike.check_bike_is_on())
        self.my_bike.toggle_power()
        self.assertTrue(self.my_bike.check_bike_is_on())

        gear = 4
        for number in range(15): self.my_bike.accelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 60)


        for number in range(6): self.my_bike.decelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 36)

        gear = 3
        for number in range(3): self.my_bike.decelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 27)

        gear = 2
        for number in range(4): self.my_bike.decelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 19)

        gear = 1
        for number in range(10): self.my_bike.decelerate(gear)
        self.assertEqual(self.my_bike.get_current_speed(), 9)

    def test_gear_speeds_are_in_ranges(self):
        self.assertFalse(self.my_bike.check_bike_is_on())
        self.my_bike.toggle_power()
        self.assertTrue(self.my_bike.check_bike_is_on())

        self.assertEqual(self.my_bike.get_current_speed(), 0)
        self.assertEqual(self.my_bike.get_current_gear(), 1)

        for number in range(21): self.my_bike.accelerate(self.my_bike.get_current_gear())
        self.assertEqual(self.my_bike.get_current_speed(), 21)
        self.assertEqual(self.my_bike.get_current_gear(), 2)

        for number in range(5): self.my_bike.accelerate(self.my_bike.get_current_gear())
        self.assertEqual(self.my_bike.get_current_speed(), 31)
        self.assertEqual(self.my_bike.get_current_gear(), 3)

        for number in range(4): self.my_bike.accelerate(self.my_bike.get_current_gear())
        self.assertEqual(self.my_bike.get_current_speed(), 43)
        self.assertEqual(self.my_bike.get_current_gear(), 4)

        self.my_bike.decelerate(self.my_bike.get_current_gear())
        self.assertEqual(self.my_bike.get_current_speed(), 39)
        self.assertEqual(self.my_bike.get_current_gear(), 3)

        for number in range(3): self.my_bike.decelerate(self.my_bike.get_current_gear())
        self.assertEqual(self.my_bike.get_current_speed(), 30)
        self.assertEqual(self.my_bike.get_current_gear(), 2)

        for number in range(5): self.my_bike.decelerate(self.my_bike.get_current_gear())
        self.assertEqual(self.my_bike.get_current_speed(), 20)
        self.assertEqual(self.my_bike.get_current_gear(), 1)

if __name__ == '__main__':
    unittest.main()