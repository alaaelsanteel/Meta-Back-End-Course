my_set={1,2,3,4,5}
#sets don't allow dublicate values
my_set.add(6) #add 6 to the set
my_set.discard(2) #delete the element 2
my_set2={6,7,8}

# joining two sets
print(my_set.union(my_set2))
print(my_set | my_set2) 

#printing the elments that existes in both sets
print(my_set.intersection(my_set2)) 
print(my_set & my_set2)

#printing the elments that existes in the first set but not the second
print(my_set.difference(my_set2))
print(my_set - my_set2)

#all elements that are in the first set or the second but not in both sets
print(my_set.symmetric_difference(my_set2))
print(my_set ^ my_set2)

#sets cannot be accessed using indexies

