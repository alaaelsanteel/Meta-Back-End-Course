
for i in range(10):  # 0 > 9
    print('looping.. ', i)

fav ={'apple','pizza','workout'} #this is a set cant access it using index 
fav2=['apple','pizza','workout'] # this is a list can be accessed using index

for indx,item in enumerate(fav):  #indx and emurate to print the index of current item
   print(indx,item)

count = 0
while count < len(fav):
    print ('I like ', fav2[count])
    count += 1

#pass to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.
#if(x == 'ss')
 #pass  #nothing happens 
