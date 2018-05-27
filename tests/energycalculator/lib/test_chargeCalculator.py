from unittest import TestCase
from energycalculator.lib import chargecalc
from energycalculator.lib.data.model.plan import Plan, Charges

class TestChargeCalculator(TestCase):
    def setUp(self):
        test_plan = Plan()
        test_plan.currency = "USD"
        energy_charges = Charges()
        energy_charges.base = 20
        energy_charges.usage_schedule = [
            UsageSchedule()
        ]
        test_plan.energy_charges = energy_charges
        self.charge_calculator = chargecalc.ChargeCalculator()

    def test_calc(self):
        self.charge_calculator
