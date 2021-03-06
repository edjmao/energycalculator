import calendar


class DiscountPowerEasy12(object):
    company_name = "Discount Power"
    plan_name = "Easy 12"

    @classmethod
    def calc(cls, kwh):
        charge = 28
        if 0 <= kwh <= 1000:
            charge += kwh * 0.0104
        if 1000 < kwh:
            charge += kwh * 0.1598
        charge += 3.49
        charge += kwh * 0.034556

        return charge


class ExpressEnergyQuick12(object):
    company_name = "Express Energy"
    plan_name = "Quick 12"

    @classmethod
    def calc(cls, kwh):
        charge = 0  # Base charge
        if kwh >= 1:
            charge = 28  # charge for 1001
        if kwh >= 1001:
            charge += 87  # Additional in excess of 1001 kwh
        if kwh > 1000:
            charge += (kwh-1000) * 0.115
        return charge


class GexaSmartChoice1000Plus12(object):
    company_name = "Gexa Energy"
    plan_name = "Right Choice 1000 Plus 12"
    
    @classmethod
    def calc(cls, kwh):
        charge = 0
        if kwh <= 499:
            charge += kwh * 0.139
        if 500 <= kwh <= 1000:
            charge += 27
        if 1000 < kwh <= 2000:
            charge += 178
        if kwh >= 2001:
            charge += kwh * 0.119

        return charge


class GexaRightChoice1000Plus12(object):
    company_name = "Gexa Energy"
    plan_name = "Right Choice 1000 Plus 12"

    @classmethod
    def calc(cls, kwh):
        charge = 0
        if kwh <= 499:
            charge += kwh * 0.119
        if 500 <= kwh <= 1000:
            charge += 27
        if 1000 < kwh <= 2000:
            charge += 188
        if kwh >= 2001:
            charge += kwh * 0.119

        return charge


class GexaRightChoice500Plus12(object):
    company_name = "Gexa Energy"
    plan_name = "Right Choice 500 Plus 12"

    @classmethod
    def calc(cls, kwh):
        charge = 0
        if kwh <= 499:
            charge += 59
        if 500 <= kwh <= 1000:
            charge += kwh * 0.0540
        if 1000 < kwh:
            charge += kwh * 0.1190

        return charge


class GexaShopperPlus12(object):
    company_name = "Gexa Energy"
    plan_name = "Gexa Shopper Plus 12"

    @classmethod
    def calc(cls, kwh):
        charge = 0
        if kwh <= 1000:
            charge += 16
        if 1000 < kwh <= 2000:
            charge += 129
        if 2000 < kwh:
            charge += kwh * 0.1190
        charge += 3.49
        charge += kwh * 0.0346
        return charge


class ChampionEnergyChampSaver12(object):
    company_name = "Champion Energy"
    plan_name = "Champ Saver-12"
    
    @classmethod
    def calc(cls, kwh):
        charge = (kwh * 0.066) + (kwh * 0.034556) + 5.68
        return charge


class FirstChoicePowerGreen12(object):
    company_name = "First Choice Power"
    plan_name = "Texas Choice Savings Green 12 - Fixed"

    @classmethod
    def calc(cls, kwh):
        charge = 0
        if 0 <= kwh <= 1000:
            charge = 28
        if kwh > 1000:
            charge = 128
        if 1000 < kwh <= 2000:
            charge += (kwh-1000) * 0.05
        if kwh > 2000:
            charge += (kwh-2000) * 0.129
        return charge


class InfiniteEnergy3MonthSmart(object):
    company_name = "Infinite Energy"
    plan_name = "3 Month Smart"

    @classmethod
    def calc(cls, kwh):
        charge = 63
        if kwh > 1000:
            charge += (kwh-1000) * 0.18
        return charge


class PowerExpressSpringSolstice12(object):
    company_name = "Power Express"
    plan_name = "Spring Solstice 12"

    @classmethod
    def calc(cls, kwh):
        charge = 18.25
        charge += 3.49
        charge += kwh * 0.0346

        if 0 <= kwh <= 1000:
            charge += kwh * 0.023
        if 1000 < kwh:
            charge += kwh * 0.144

        return charge


def print_annual_table(plans, usage_history):
    plan_sums = [0 for i in range(0, len(plans))]
    for (month, usage) in zip(calendar.month_abbr[1:], usage_history):
        line = "{} ({:>4}):".format(month, usage)
        values = [plan.calc(usage) for plan in plans]
        plan_sums = [existingsum + val for (existingsum, val) in zip(plan_sums, values)]
        line += "".join([" {:>8.2f}".format(val) for val in values])
        print(line)
    print("           {}".format("".join([" {:>8.2f}".format(plan) for plan in plan_sums])))


if __name__=="__main__":

    plans = [
        # GexaRightChoice500Plus12,
        GexaRightChoice1000Plus12,
        GexaSmartChoice1000Plus12,
        # GexaShopperPlus12,
        # DiscountPowerEasy12,
        # PowerExpressSpringSolstice12,
        ChampionEnergyChampSaver12,
         ]
    usage_array = [x for x in range(0, 2500, 100)]
    usage_history = [1000, 851, 818, 785, 986, 1466, 1708, 1233, 1107, 902, 743, 874]

    for usage in usage_array:
        line = "{:>6}:".format(usage)
        line += "".join([" {:>7.2f}".format(plan.calc(usage)) for plan in plans])
        print(line)

    print_annual_table(plans, usage_history)
    print_annual_table(plans, [usage + 100 for usage in usage_history])
    print_annual_table(plans, [usage + 200 for usage in usage_history])
    print_annual_table(plans, [usage - 100 for usage in usage_history])
