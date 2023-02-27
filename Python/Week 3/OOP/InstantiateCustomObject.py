class example():
    #The __new__ method for creating and returning a new empty object
    def __new__(cls: type[Self]) -> Self:
        pass
    #CLS not a keyword it's a convention it acts like a placeholder for passing the class as it's first argument
    #for creating the new empty object

    #The __init__constructor method
    #it takes the object created by the new method (as it's first arg)to initialize the new object that is being created
    def __init__(self) -> None:
        pass
    #the self keyword is another convention it has no function itself but serves as a placeholder for self-refrence
    #by its instance object
class recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items=items
        self.time= time
    def contents(self):
        print("The "+self.dish+"has "+str(self.items)+"and takes "+ str(self.time)+"min to preper")

 #creating objects       
pizza= recipe("Pizza",["chesse","bread","tomato"],45)
pasta = recipe("Pasta",["penne","sauce",],50)

print (pizza.items) #["chesse","bread","tomato"]
print(pizza.contents()) #The Pizza has ["chesse","bread","tomato"] and takes 45 min to preper
