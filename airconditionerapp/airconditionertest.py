import unittest
from airconditioner import AirConditioner

class AirConditionerTest(unittest.TestCase):

    def setUp(self):
        self.my_ac = AirConditioner()

    def test_air_conditioner_is_on(self):
        self.assertFalse(self.my_ac.check_ac_is_on())
        self.my_ac.toggle_power()
        self.assertTrue(self.my_ac.check_ac_is_on())

    def test_air_conditioner_is_off(self):
        self.assertFalse(self.my_ac.check_ac_is_on())
        self.my_ac.toggle_power()
        self.assertTrue(self.my_ac.check_ac_is_on())

        self.my_ac.toggle_power()
        self.assertFalse(self.my_ac.check_ac_is_on())

    def test_temperature_increases(self):
        self.my_ac.toggle_power()
        self.assertTrue(self.my_ac.check_ac_is_on())
        self.assertEqual(self.my_ac.get_temperature(), 24)

        self.my_ac.increase_temperature(5)
        self.assertEqual(self.my_ac.get_temperature(), 29)

    def test_temperature_decreases(self):
        self.my_ac.toggle_power()
        self.assertTrue(self.my_ac.check_ac_is_on())
        self.assertEqual(self.my_ac.get_temperature(), 24)

        self.my_ac.decrease_temperature(5)
        self.assertEqual(self.my_ac.get_temperature(), 19)

    def test_temperature_increase_does_not_exceed_30(self):
        self.my_ac.toggle_power()
        self.assertTrue(self.my_ac.check_ac_is_on())
        self.assertEqual(self.my_ac.get_temperature(), 24)
        self.my_ac.increase_temperature(6)
        self.assertEqual(self.my_ac.get_temperature(), 30)

        self.my_ac.increase_temperature(5)
        self.assertEqual(self.my_ac.get_temperature(), 30)

    def test_temperature_decrease_does_not_exceed_16(self):
        self.my_ac.toggle_power()
        self.assertTrue(self.my_ac.check_ac_is_on())
        self.assertEqual(self.my_ac.get_temperature(), 24)
        self.my_ac.decrease_temperature(4)
        self.assertEqual(self.my_ac.get_temperature(), 20)

        self.my_ac.decrease_temperature(10)
        self.assertEqual(self.my_ac.get_temperature(), 16)

if __name__ == '__main__':
    unittest.main()
