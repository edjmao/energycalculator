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
                    UsageSchedule(
                        lower=0,
                        upper=100
                    ),
                    UsageSchedule(
                        lower=100,
                        upper=500,
                        fixed_charge=28,
                    )
                ]
            )
        )
        self.charge_calculator = chargecalc.ChargeCalculator(self.test_plan)

    def test_calc_base(self):
        charge = self.charge_calculator.calc(50)
        self.assertEqual(20, charge)

    def test_calc_fixed(self):
        charge = self.charge_calculator.calc(200)
        self.assertEqual(48, charge)

    def test_create(self):
        self.assertEqual("USD", self.test_plan.currency)