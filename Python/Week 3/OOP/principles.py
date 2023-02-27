#Encapsulation is also used for hiding data and its internal representation but python use inhertance to apply it
#
class Alpha:

 def __init__(self):
    self._a = 2.  # Protected member ‘a’
    self.__b = 2.  # Private member ‘b’
#self._a is a protected member and can be accessed by the class and its subclasses
#self.__b is a private member of the class Alpha and can only be accessed from within the class Alpha.
#these private and protected members can still be accessed from outside of the class by 
# using public methods to access them or by a practice known as name mangling. 
#Name mangling is the use of two leading underscores and one trailing underscore
# for example:
# _class__identifier 
#Class is the name of the class and identifier is the data member that I want to access.

#Polymorphism refers to something that can have many forms.
#operator, method or any object of some class. 
#I can illustrate the case for polymorphism using built-in functions and operations, for example:
string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)
#OUTPUT : polypolypoly 21 [1, 2, 3, 1, 2, 3, 1, 2, 3]
# have used the same operator () in the print to perform on a string, 
# integer and a list. You can see the () operator behaves differently in all three cases.

#Inheritance in Python will be covered later in the course, but the basic template for it is as follows:
#class Parent:
    #Members of the parent class

#class Child(Parent):
    #Inherited members from parent class
    #Additional members of the child class

#Method Resolution Order (MRO)
#that determines the flow of execution. MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity,

#Abstraction can be seen both as a means for hiding important information 
# as well as unnecessary information in a block of code
#bstract classes and methods, which can be implemented by inheriting from something called the abc module.
#  "abc" here stands for abstract base class.
#  It is first imported and then used as a parent class for some class that becomes an abstract class. 
from abc import ABC
class ClassName(ABC):
    pass