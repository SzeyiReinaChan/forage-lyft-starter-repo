import unittest
from datetime import datetime
from battery.nubbinBattery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_services(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 6)

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())