def calculate_tax (bill, tax_rate):
    return round((bill * tax_rate)/100.00)

print('Total Tax', calculate_tax(175.00, 15))

# Variable Scope
#Global Scope
globale_v = 2

def fn1():
 
 enclosed_v=10

 def fn2():
       local_v=5
       print(enclosed_v)
##Global scope is when a variable is declared outside of a function
#Local scope refers to a variable declared inside a function
#Enclosing scope refers to a function inside another function or what is commonly called a nested function
#enclosed variable declared in the outer function
#Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in

 