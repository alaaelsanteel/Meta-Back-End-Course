def d():
    animal="elephant"
    def e():
        nonlocal animal #changing the value
        animal="giraffe"
        print("inside nested function "+ animal) #giraffe
    print("before calling function: "+ animal)#elephant
    e()
    print("after calling the function: "+animal)#giraffe

animal ="camel"
d()
print("Global variable "+animal)#camel