menu = ["espresso", "mocha","latte","cappuccino","cortado","americano"]

def find_coffee(coffee):
    if coffee[0]== 'c':
        return coffee
    
map_coffee = map(find_coffee,menu)  #function and a list to search in as a parameter for the function

print(map_coffee)

for x in map_coffee:
        print(x)

filter_map= filter(find_coffee,menu)
for x in filter_map:
    print(x)
# Maps take all objects in a list and applies a function >> Applies function to every item in an iterable
# filters do the same, but take the results and create a list with only the  true value >>returns
#  all elements of an iterable when function returns True
