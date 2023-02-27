print('Hello, World')
x =1 +    2 \
+ 3  
#\ connecting the two lines 
#any ammount of whitespace on a single line is ok
def say_hello(): print("Hello there!")
#or
def say_hello(): 
    print("Hello there!")

name ="john"
if name == "john":
    print(name)

a= b = c =10 #all equal to 10
a, b, c = 1, 2, 3

a = 10
print (a) #10
a = 5
print(a) #5

del a # delete
print (a) # a is not defined 

# list = array accessed by index
ex_list = [1,'adaf',"A",4.5] 

#Tubles contain ordered sequence of on or more types,they are immutabl the values cannot be changed accessed by index
ex_Tuble = (1,'adaf',"A",4.5) 

#Dictionary accessed by the key
ed ={'a':22, 'b':33}
print(ed['a'])
#Set unordered or non-indexed collection
ex_set ={1,'adaf',"A",4.5 }
#string length
s='john'
ss= 'mark'
len(s)
print(s + ss) # connecting two string

#input
print("Where do you live?")
location = input()
print("So you live in " + location)

location = input("Where do you live?")

#convert to string
str(55) #'55'

#convert to int
int('75') #75

#convert to float
some_int = 10
float(some_int) #10.0

#create a function
def name_fun():
    return 1
def say_name(you):
    return "your name is" + you

  #Data Casting
  # Implicit and Explicit
  # Implicit : automatically by python's comppiler to prevent data loss   
  # Explicit : using built-in functions


  #ord() : the unicode character
  #hex() : to hexa
  #oct() : to octal
  #tuple(), set(), list(), dic()

#print
print("Hello","you!", sep=', ') # separeted by comma

num1= input()
num2=input()
print(num1 + num2) # num1=1 ,num2 =2 >>12 
print(int(num1)+int(num2)) >>3


num_1 = input('First number is: ')
num_2 = input('Second number is: ')
user_sum = float(num_1) + float(num_2)
print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum) #error

n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)
print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))




