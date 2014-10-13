#bike_industry.py
#Test bike industry oop architecture

import oop_bikeshop as bikes
import random
import pdb


def main():
    #Set seed:
    random.seed(20)
    #Create wheels:
    wheel_options = [bikes.Wheel("Carbon",5,45), bikes.Wheel("Steel",10,5), bikes.Wheel("Aluminium", 7.2, 25)]
    #Create frames:
    frame_options = [bikes.Frame("Carbon",10,300), bikes.Frame("Steel",20,40), bikes.Frame("Aluminium", 16.4, 150)]
    #Create bikes
    bike_options = [bikes.Bike("SlowRider", random.choice(wheel_options), random.choice(frame_options)),
                    bikes.Bike("MegaFaster", random.choice(wheel_options), random.choice(frame_options)),
                    bikes.Bike("Mr. Blingy", random.choice(wheel_options), random.choice(frame_options)),
                    bikes.Bike("CokeZero", random.choice(wheel_options), random.choice(frame_options)), 
                    bikes.Bike("MontyZooma", random.choice(wheel_options), random.choice(frame_options)), 
                    bikes.Bike("Trekker", random.choice(wheel_options), random.choice(frame_options))]   
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









