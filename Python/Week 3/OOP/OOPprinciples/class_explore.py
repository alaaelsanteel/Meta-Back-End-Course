class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a) 

print("Instantiating B..")
b = B(a)
print(a)
#line 24, 28 print tha address of the object instead of content
#the address of object a is the same both inside class B
#and in the global scope of the program. It remains the same irrespective of from where it is called
#he alpha() function is called twice in the program, but you still get the output as 2 every time and not 3
# That's because the value is updated only temporarily and not assigned to anything.

