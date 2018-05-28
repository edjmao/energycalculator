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
                    ),
                    UsageSchedule(
                        lower=500,
                        upper=1000,
                        per_kwh_charge=.1
                    ),
                    UsageSchedule(
                        lower=1000,
                        upper=1500,
                        fixed_charge=10,
                        per_kwh_charge=.1
                    ),
                    UsageSchedule(
                        lower=2000,
                        fixed_charge=100
                    )
                ]
            )
        )
        self.charge_calculator = chargecalc.ChargeCalculator(self.test_plan)

    def test_calc_base(self):
        charge = self.charge_calculator.calc(50)
        self.assertEqual(20.0, charge)

    def test_calc_fixed(self):
        charge = self.charge_calculator.calc(200)
        self.assertEqual(48.0, charge)

    def test_calc_per_kwh(self):
        charge = self.charge_calculator.calc(500)
        self.assertEqual(70.0, charge)

    def test_calc_and_per_kwh(self):
        charge = self.charge_calculator.calc(1000)
        self.assertEqual(130, charge)

    def test_calc_no_base(self):
        self.test_plan.energy_charges.base=None
        charge = self.charge_calculator.calc(50)
        self.assertEqual(0, charge)

    def test_calc_unbounded_upper(self):
        charge = self.charge_calculator.calc(2500)
        self.assertEqual(120, charge)

    def test_calc_not_found(self):
        charge = self.charge_calculator.calc(1750)
        self.assertEqual(20, charge)

    def test_calc_service_charge(self):
        self.test_plan.delivery_charges = Charges(
            base=10,
            usage_schedule=[UsageSchedule(
                lower=0,
                per_kwh_charge=.1
            )]
        )
        charge = self.charge_calculator.calc(100)
        self.assertEqual(68, charge)

    def test_create(self):
        self.assertEqual("USD", self.test_plan.currency)