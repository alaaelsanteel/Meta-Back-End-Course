#args and kargs are Keyword arguments and Non-keyword variables
def sum_of(*args): #*args to accept any number of arguments
    sum=0
    for i in args:
        sum += i
    return sum

print(sum_of(4,3,6,5))

def sum_of(**kargs): #*args to accept any number of arguments that is assigned to a name
    sum=0
    for k,v in kargs.items():
        sum += v
    return sum

print(sum_of(coffee=2.44,cake=3,juice=2.99))

