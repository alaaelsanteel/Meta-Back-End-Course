class Employee:
    def __init__(self, name, last) -> None:
     self.name= name 
     self.last = last
class supervisoers(Employee):
    def __init__(self, name, last,password) -> None:
       super().__init__(name, last)
       self.password = password
class chefs(Employee):
    def leave_req(self,days):
        return "May I take a leave for "+str(days) +" days"

adrian=supervisoers("adrian","A","apple")

emily= chefs("emily","e")
juno = chefs("juno","J")
print(emily.leave_req(3))
print(adrian.password)
print(juno.name)

#If you change anything inside the parent class
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()
#output >>Fruit type:  Apple Apple is sweet
#Built-in functions
#issubclass(class A, class B)
#isinstance(b,B)

#Multi-level inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)