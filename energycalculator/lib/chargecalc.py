
class ChargeCalculator(object):
    """Charge calculator

    Calculates the charge of a given plan.
    """

    def __init__(self, plan):
        self.plan = plan

    def calc(self, kwh):
        total_charge = 0
        energy_charge = self.plan.energy_charges
        total_charge += energy_charge.base
        return total_charge
