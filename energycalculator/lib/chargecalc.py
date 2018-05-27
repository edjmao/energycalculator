import logging

class ChargeCalculator(object):
    """Charge calculator

    Calculates the charge of a given plan.
    """

    def __init__(self, plan):
        self.plan = plan

    def calc(self, kwh):
        def _filter_schedule(schedule):
            if(schedule.lower is None):
                logging.warning("Schedule has a None lower kWh limit")
                return False
            if (schedule.upper is None):
                return schedule.lower <= kwh
            return schedule.lower <= kwh < schedule.upper

        def _calc_charge(schedule):
            schedule_charge = 0
            if(schedule.fixed_charge is not None):
                schedule_charge += schedule.fixed_charge
            if(schedule.per_kwh_charge is not None):
                schedule_charge += schedule.per_kwh_charge * kwh
            return schedule_charge

        total_charge = 0
        energy_charge = self.plan.energy_charges
        total_charge += energy_charge.base

        applicable_schedules = list(filter(_filter_schedule, energy_charge.usage_schedule))
        fixed_charges = sum(map(_calc_charge, applicable_schedules))
        total_charge += fixed_charges
        return total_charge
