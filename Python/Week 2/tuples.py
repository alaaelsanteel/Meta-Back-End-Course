my_tuble= (1,'hello',55.4,True)
print(my_tuble[1]) #hello
print(type(my_tuble)) #class tuple
print(my_tuble.count('hello'))  #1
print(my_tuble.index(55.4)) #2

#Tubles are immutable >values cann't be changed
my_tuble[0]=2  #typeError