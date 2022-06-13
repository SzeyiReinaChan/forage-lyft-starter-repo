import unittest
from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_not_need_service(self):
        tire_wear = [0.6, 0.6, 0.6, 0.6]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
