import calendar


class DiscountPowerEasy12(object):
    company_name = "Discount Power"
    plan_name = "Easy 12"

    @classmethod
    def calc(cls, kwh):
        return 20+3.49+(kwh*3.4556+1.83*min(1000,kwh)+14.59*max(0,kwh-1000))/100


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


class GexaRightChoice1000Plus12(object):
    company_name = "Gexa Energy"
    plan_name = "Right Choice 1000 Plus 12"
    
    @classmethod
    def calc(cls, kwh):
        charge = 0
        if kwh <= 500:
            charge += 39
        if 500 < kwh < 1000:
            charge += 99
        if 1000 <= kwh <= 1500:
            charge += kwh * 0.028
        if 1500 < kwh <= 2000:
            charge += 178
        if kwh > 2000:
            charge += kwh * 0.109

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


def printAnnualTable(plans, usage_history):
    plan_sums = [0 for i in range(0, len(plans))]
    for (month, usage) in zip(calendar.month_abbr[1:], usage_history):
        line = "{} ({:>4}):".format(month, usage)
        values = [plan.calc(usage) for plan in plans]
        plan_sums = [existingsum + val for (existingsum, val) in zip(plan_sums, values)]
        line += "".join([" {:>8.2f}".format(val) for val in values])
        print(line)
    print("           {}".format("".join([" {:>8.2f}".format(plan) for plan in plan_sums])))


if __name__=="__main__":

    plans = [DiscountPowerEasy12,
             ExpressEnergyQuick12,
             GexaRightChoice1000Plus12,
             ChampionEnergyChampSaver12,
             FirstChoicePowerGreen12,
             InfiniteEnergy3MonthSmart]
    usage_array = [x for x in range(0, 2500, 100)]
    usage_history = [1000, 851, 818, 785, 986, 1466, 1708, 1233, 1107, 902, 743, 874]

    for usage in usage_array:
        line = "{:>6}:".format(usage)
        line += "".join([" {:>7.2f}".format(plan.calc(usage)) for plan in plans])
        print(line)

    printAnnualTable(plans, usage_history)
    printAnnualTable(plans, [usage + 100 for usage in usage_history])
    printAnnualTable(plans, [usage + 200 for usage in usage_history])
    printAnnualTable(plans, [usage - 100 for usage in usage_history])
