
class ChargeCalculator(object):
    """Charge calculator

    Calculates the charge of a given plan.
    """

    def __init__(self, plan):
        self.plan = plan

    def calc(self, kwh):
        energy_charge = self.plan.energy_charges
        return None
