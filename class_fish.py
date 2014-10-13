#aquaria_objects.py


class aquarium(object):
    fish = []
    def __init__(self, fish):
        self.fish = fish

    def feed_fish(self, food):
        print "Starting to feed fish!"
        for fish in self.fish:
            fish.eat(food)
        
class fish(object):
    hunger_level = 'hungry'
    speed = 'slow'
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.hunger_level = "Not hungry"
        print self.name + "is eating " + food + "!"

class shark(fish):
    color = 'grey'
    speed = 'fast'

class goby(fish):
    color = 'yellow'
    speed = 'stopped'







