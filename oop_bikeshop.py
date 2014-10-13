import random
import pdb

class Wheel(object):
    wheeltype = "Default Type"
    weight = 10
    cost = 45

    def __init__(self,wheeltype,weight, cost):
        self.wheeltype = wheeltype
        self.weight = weight
        self.cost = cost

class Frame(object):
    name = "Default Name"
    weight = 20
    cost = 40

    def __init__(self,name,weight,cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class Bike(object):
    "Bike base class"
    name = "Generic Bike"
    weight = 1
    base_cost = 1
    
    def __init__(self,name, wheel_object, frame_object):
        self.name = name
        self.wheel_list = []
        self.frame = []
        for i in range(0,2):
            self.wheel_list.append(wheel_object)
        self.frame.append(frame_object)
        self.weight = self.calculate_weight()
        self.base_cost = self.calculate_cost()

    def calculate_weight(self):
        self.wheel_weight = sum([wheel_object.weight for wheel_object in self.wheel_list])
        self.frame_weight = self.frame[0].weight
        return self.wheel_weight + self.frame_weight

    def calculate_cost(self):
        self.wheel_cost = sum([wheel_object.cost for wheel_object in self.wheel_list])
        self.frame_cost = self.frame[0].cost
        return self.wheel_cost + self.frame_cost

class Bikeshop(object):
    "Ye olde bike shoppe base class"
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












