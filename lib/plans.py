
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
        charge = 0 # Base charge
        if kwh >= 1:
            charge = 28 # charge for 1001
        if kwh >= 1001:
            charge += 87 # Additional in excess of 1001 kwh
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
        if kwh > 500 and kwh < 1000:
            charge += 99
        if kwh >= 1000 and kwh <= 1500:
            charge += kwh * 0.028
        if kwh > 1500 and kwh <= 2000:
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

if __name__=="__main__":

    plans = [DiscountPowerEasy12, ExpressEnergyQuick12, GexaRightChoice1000Plus12, ChampionEnergyChampSaver12]
    usage_array = [ x for x in range(0, 2500, 100)]

    for usage in usage_array:
        #print("%s - %s" % (plan.company_name, plan.plan_name))
        line = "{:>6}:".format(usage)
        line += "".join([ " {:>7.2f}".format(plan.calc(usage)) for plan in plans ])
        print(line)
