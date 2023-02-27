class myClass:
    pass #noting to execute

class newC:
    a=5
    print("Hello")
    def hello():
        print("Hey There!")

obj =newC() #Hello
print(newC.a) #5 == print(obj.a) attribute references still works with instancw objects
print(newC.hello()) #Error
#resolve this error by adding self in the function parentheses

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House()
print(house.num_rooms) #5
print(House.num_rooms) #5

house.num_rooms = 7
print(house.num_rooms) #7
print(House.num_rooms) #5
#It updates the value of the instance attribute, but not the class attribute

House.num_rooms = 7
print(house.num_rooms) #7
print(House.num_rooms) #7
#Example
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost
house = House()
print(house.num_rooms) #5
print(House.num_rooms) #5
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms) #7
print(House.num_rooms) #5
