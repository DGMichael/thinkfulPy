import random

class Bike(object):
    "Bike base class"
    name = "Generic Bike"
    weight = 20
    base_cost = 100

    def __init__(self,name, weight, base_cost):
        self.name = name
        self.weight = weight
        self.base_cost = base_cost
        
class Bikeshop(object):
    "Bike shope base class"
    shop_name = "Bike Shop"
    markup = 0
    bike_profit = 0
    inventory = {}

    def __init__(self, shop_name, markup):
        self.shop_name = shop_name
        self.markup = markup

    def stock_bike(self, bike_object, num_stocked):
        """Stock bike in inventory data structure"""
        if bike_object.name not in self.inventory.keys():
            self.inventory[bike_object.name] = [bike_object, num_stocked]
        else:
            self.inventory[bike_object.name][1] += num_stocked

    def display_inventory(self):
        print "Currently in inventory:"
        for bike in self.inventory.keys():
            print self.inventory[bike][0].name + " " + str(self.inventory[bike][1])

    def print_stock_in_budget(self, customer_budget, customer_name):
        print "These are the bikes that {0} can afford:".format(customer_name)
        for bike in self.inventory.keys():
            if (self.inventory[bike][0].base_cost * self.markup) < customer_budget and self.inventory[bike][1] > 0:
                print self.inventory[bike][0].name

    def gen_possible_bikes(self, customer_budget):
        self.possible_bikes = []
        for bike in self.inventory.keys():
            if (self.inventory[bike][0].base_cost * self.markup) < customer_budget and self.inventory[bike][1] > 0:
                self.possible_bikes.append(self.inventory[bike][0])
        return self.possible_bikes

    def inform_cost(self, bike_choice):
        return(bike_choice.base_cost * self.markup)

    def sell_bike(self, bike_name, num_sold):
        self.inventory[bike_name][1] -= num_sold
        self.bike_profit += (self.inventory[bike_name][0].base_cost * self.markup) * num_sold

    def report_status(self):
        self.display_inventory()
        print "Total profit: $" + str(self.bike_profit)


class Customer(object):
    "Customer base class.  Assumed to have no bikes upon instantiation."
    name = "Default Name"
    funds = 0
    bikes_owned = []

    def __init__(self,name, funds):
        self.name = name
        self.funds = funds

    def choose_bike(self, possible_bikes):
        self.bike_choice = random.choice(possible_bikes)
        return self.bike_choice

    def buy_bike(self, bike_object, bike_cost):
        self.funds -= bike_cost
        self.bikes_owned.append(bike_object)












