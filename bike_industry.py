#bike_industry.py
#Test bike industry oop architecture

import oop_bikeshop as bikes
import random
import pdb


def main():
    #Create bikes
    bike_options = [bikes.Bike("SlowRider", 20, 110), bikes.Bike("MegaFaster",11,380), bikes.Bike("Mr. Blingy", 12,730),
                       bikes.Bike("CokeZero", 13,220), bikes.Bike("MontyZooma", 19,330), bikes.Bike("Trekker", 40,120)]   
    bike_list = [bike.name for bike in bike_options]
    #Create bike shop, add inventory:
    mikes_shop = bikes.Bikeshop("Mikes Shop", 1.2)
    for bike in bike_options:
        mikes_shop.stock_bike(bike, random.randint(1,30))
    print "Mikes Shop Now OPEN for the day!"
    mikes_shop.display_inventory()
    #Generate customers:
    customer_list = [bikes.Customer("Homer",200), bikes.Customer("Smithers", 500), bikes.Customer("Mr. Burns", 1000)]
    #ID and sell bikes:
    for customer in customer_list:
        print "{0} has just come in the shop!".format(customer.name)
        mikes_shop.print_stock_in_budget(customer.funds, customer.name)
        bikes_in_budget = mikes_shop.gen_possible_bikes(customer.funds)
        bike_choice = customer.choose_bike(bikes_in_budget)
        bike_cost = mikes_shop.inform_cost(bike_choice)
        customer.buy_bike(bike_choice, bike_cost)
        mikes_shop.sell_bike(bike_choice.name, 1)
        print "{0} chose the {1} at a cost of ${2} and has ${3} left.".format(customer.name, bike_choice.name, bike_cost, customer.funds)
    print "End of day status for Mike's Shop: "
    mikes_shop.report_status()

main()









