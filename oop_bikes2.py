#Objects for bike industry 2.0:

import random
import pdb

class Wheel(object):
    "Base wheel class"
    def __init__(self,name, weight, cost):
        self.name = name
        self.weight  = weight
        self.cost = cost

class Frame(object):
    "Base frame class"
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class Bike(object):
    "Base bike class"
    def __init__(self, bike_feature_tuple, parts_dict):
        bike_name, wheel_type, frame_type = bike_feature_tuple 
        self.name = bike_name
        wheel_name, wheel_weight, wheel_cost = parts_dict[wheel_type]
        self.wheel_list = [Wheel(wheel_name, wheel_weight, wheel_cost), Wheel(wheel_name, wheel_weight, wheel_cost)]
        frame_name, frame_weight, frame_cost = parts_dict[frame_type]
        self.frame = Frame(frame_name, frame_weight, frame_cost)
        self.cost = self.calculate_cost()
        self.weight = self.calculate_weight()

    def calculate_cost(self):
        wheel_cost = sum([wheel.cost for wheel in self.wheel_list])
        return wheel_cost + self.frame.cost

    def calculate_weight(self):
        wheel_weight = sum([wheel.weight for wheel in self.wheel_list])
        return wheel_weight + self.frame.weight

class Bike_shop(object):
    "Base bikeshop class"
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inv_objectDict = {}
        self.inv_numDict = {}
        self.bike_profit = 0

    def stock_bike(self, bike_name, num_stocked, bike_dict, parts_dict):
        "Stock bike in inventory"
        bike_feature_tuple = bike_dict[bike_name]
        if bike_name not in self.inv_objectDict.keys() and bike_name not in self.inv_numDict.keys(): #Bike not previously stocked, add object and number
            self.inv_objectDict[bike_name] = Bike(bike_feature_tuple, parts_dict)
            self.inv_numDict[bike_name] = num_stocked
        elif bike_name in self.inv_objectDict.keys() and bike_name in self.inv_numDict.keys(): #Bike previously stocked, add number to existing stock
            self.inv_numDict[bike_name] += num_stocked

    def display_inv(self):
        print "Current {0} Inventory:".format(self.name)
        for bike in self.inv_objectDict.keys():
            bike_object = self.inv_objectDict[bike]
            num_bikes = self.inv_numDict[bike]
            print "{0}: {1}".format(bike_object.name, num_bikes)

    def print_stock_in_budget(self, customer, num_desired):
        print "These are the bikes that {0} can afford:".format(customer.name)
        for bike in self.inv_objectDict.keys():
            bike_object = self.inv_objectDict[bike]
            if (bike_object.cost * self.margin * num_desired) < customer.funds and self.inv_numDict[bike] >= num_desired:
                print bike_object.name

    def gen_possible_options(self, customer, num_desired):
        possible_bikes = []
        for bike in self.inv_objectDict.keys():
            bike_object = self.inv_objectDict[bike]
            if (bike_object.cost * self.margin * num_desired) < customer.funds and self.inv_numDict[bike] >= num_desired:
                possible_bikes.append(bike_object.name)
        return possible_bikes

    def report_cost (self, bike_name):
        bike_object = self.inv_objectDict[bike_name]
        return bike_object.cost * self.margin

    def sell_bike(self, bike_name, num_bought):
        bike_object = self.inv_objectDict[bike_name]
        self.bike_profit += (bike_object.cost * self.margin - bike_object.cost) * num_bought 
        self.inv_numDict[bike_name] -= int(num_bought)

    def report_status(self):
        print "Total profit: {0}".format(self.bike_profit)

class Customer(object):
    "Base customer class"
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.inv_bikes = []

    def choose_bike(self, possible_bikes):
        return random.choice(possible_bikes)

    def buy_bike(self, bike_feature_tuple, bike_cost, num_bought, parts_dict):
        for i in range(0,num_bought):
            self.funds -= bike_cost
            self.inv_bikes.append(Bike(bike_feature_tuple, parts_dict))












