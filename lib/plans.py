
class DiscountPowerEasy12:
    company_name = "Discount Power"
    plan_name = "Easy 12"

    @classmethod
    def calc(cls, kwh):
        return 20+3.49+(kwh*3.4556+1.83*min(1000,kwh)+14.59*max(0,kwh-1000))/100

if __name__=="__main__":
    print("%s - %s" % (DiscountPowerEasy12.company_name, DiscountPowerEasy12.plan_name))

    usage_array = [ x for x in range(0, 2001, 100)]

    for usage in usage_array:
        print("{:>6}: {:.2f}".format(usage, DiscountPowerEasy12.calc(usage)))
