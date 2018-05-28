import logging


class ChargeCalculator(object):
    """Charge calculator

    Calculates the charge of a given plan.
    """

    def __init__(self, plan):
        self.plan = plan

    def calc(self, kwh):
        def _filter_schedule(schedule):
            if schedule.lower is None:
                logging.warning("Schedule has a None lower kWh limit")
                return False
            if schedule.upper is None:
                return schedule.lower <= kwh
            return schedule.lower <= kwh < schedule.upper

        def _calc_charge(schedule):
            schedule_charge = 0
            if schedule.fixed_charge is not None:
                schedule_charge += schedule.fixed_charge
            if schedule.per_kwh_charge is not None:
                schedule_charge += schedule.per_kwh_charge * kwh
            return schedule_charge

        def _calc_charges(charge):
            calc_charge = 0
            if charge:
                if charge.base is not None:
                    calc_charge += charge.base
                calc_charge += sum(map(_calc_charge, list(filter(_filter_schedule, charge.usage_schedule))))
            return calc_charge

        total_charge = 0
        total_charge += _calc_charges(self.plan.energy_charges) + _calc_charges(self.plan.delivery_charges)

        return total_charge
