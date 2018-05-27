from unittest import TestCase
from energycalculator.lib import chargecalc
from energycalculator.lib.data.model.plan import Plan, Charges, UsageSchedule


class TestChargeCalculator(TestCase):
    def setUp(self):
        self.test_plan = Plan(
            currency="USD",
            energy_charges=Charges(
                base=20,
                usage_schedule=[
                    UsageSchedule()
                ]
            )
        )
        self.charge_calculator = chargecalc.ChargeCalculator(self.test_plan)

    def test_calc(self):
        charge = self.charge_calculator.calc(100)
        self.assertEqual(20, charge)

    def test_create(self):
        self.assertEqual("USD", self.test_plan.currency)