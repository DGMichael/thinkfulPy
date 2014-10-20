#bike_industry 2.0

import oop_bikes2 as bikes
import random

def main():
    #random.seed(20)
    #Generate frame, wheel and bike options:
    frame_choices = ["carbon frame", "steel frame", "aluminium frame"]
    wheel_choices = ["carbon wheel", "steel wheel", "aluminium wheel"]
    parts_dict = {"carbon wheel":('carbon wheel', 2.5, 50),
                    "aluminium wheel":('aluminium wheel', 5, 25),
                    "steel wheel":('steel wheel', 10, 12),
                    "carbon frame":('carbon frame', 10, 100),
                    "aluminium frame": ('aluminium frame', 20,50),
                    "steel frame": ("steel frame", 40, 50)}
    bike_dict = {"MontyZooma":("MontyZooma", random.choice(wheel_choices), random.choice(frame_choices)),
                    "PearlZoomie": ("PearlZoomie", random.choice(wheel_choices), random.choice(frame_choices)),
                    "Zoomba": ("Zoomba", random.choice(wheel_choices), random.choice(frame_choices)),
                    "Roomba": ("Roomba", random.choice(wheel_choices), random.choice(frame_choices)),
                    "PinoZiip": ("PinoZiip", random.choice(wheel_choices), random.choice(frame_choices)),
                    "SlowRider": ("SlowRider", random.choice(wheel_choices), random.choice(frame_choices))}
    #Create bikeshop and inventory:
    mikes_shop = bikes.Bike_shop("Mikes Shop", 1.2)
    for bike_name in bike_dict.keys():
        bike_feature_tuple = bike_dict[bike_name]
        mikes_shop.stock_bike(bike_name, random.randint(1,10), bike_dict, parts_dict)
    print "{0} is now open for the day!".format(mikes_shop.name)
    #Generate customers:
    customer_list = [bikes.Customer("Homer",200), bikes.Customer("Smithers", 750), bikes.Customer("Mr. Burns", 10000)]
    #ID and sell bikes:
    for customer in customer_list:
        print "{0} has just come into the shop!".format(customer.name)
        bikes_in_budget = []
        while len(bikes_in_budget) == 0:
            num_desired = random.randint(1,5)
            bikes_in_budget = mikes_shop.gen_possible_options(customer, num_desired)
        bike_choice = customer.choose_bike(bikes_in_budget)
        mikes_shop.print_stock_in_budget(customer, num_desired)
        bike_cost = mikes_shop.report_cost(bike_choice)
        mikes_shop.sell_bike(bike_choice, num_desired)
        customer.buy_bike(bike_dict[bike_choice], bike_cost, num_desired, parts_dict)
        print "{0} choose to buy {1} of {2} at a cost of {3} each.".format(customer.name, num_desired, bike_choice, bike_cost)
        print "{0} current bike inventory is:".format(customer.name)
        for bike in customer.inv_bikes:
                print bike.name
    print "Closing up shop for the day."
    mikes_shop.report_status()

main()









