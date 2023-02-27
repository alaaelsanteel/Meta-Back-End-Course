#types of Inheritance
#simple inheritance (child and parent class)
#multiple inheritance (child class inheriting from more than one parent class )
#multi leverl inhertience (inheritace taking place in several levels > child>child>parent)
#hirearchical inheritance(subclasses inherit from a parent class)
#Hybrid inheritance (mixes the characteristics of the others)

# Method Resolution Order : determines the order in which a given method or attribute passed is searched(from where it belongs)
# order of resolution is called linearization
#defualt order in python is bottom to up ,left to right
# the object first search in the class its from and then the parent class
# class x       class y
#        class z     (inherits from both)
#MRO >>z >> x >> y  >>bottom>>up>>left>>right
#  we rely on Algorithms to build MROs 
# Old style classes used Depth-First Search(DFS) from V3 it relys on C3 Linearization Algorithm
# C3 Linearization 
# 1- Adheres Monotonicity : an inherited property cannot skip over direct parent classes
# 2- follows the inheritance graph
# 3- visits Super class after visiting local class  

class A:
    num = 5
class B(A):
    num=9
class C(B):
 pass
print(C.mro()) #[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(C.help()) #much more details than the more
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(B,A):
    pass

# Driver code
c = C()
print(c.a()) #Function inside B

class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    def b(self):
        return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b()) #Function inside C

class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d()) #Function inside E
print(F.mro()) #[<class '__main__.F'>, <class '__main__.E'>, 
#<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]