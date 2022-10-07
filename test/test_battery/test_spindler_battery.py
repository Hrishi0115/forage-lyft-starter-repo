import unittest
from datetime import date
from battery.spindlerBattery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-10-07")
        last_service_date = date.fromisoformat("2020-05-05")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-07-10")
        last_service_date = date.fromisoformat("2021-05-05")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


