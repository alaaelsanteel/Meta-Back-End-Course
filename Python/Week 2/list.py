list1=[1,2,3,4]
list2=[1,'hello',True,40.44]
list3=[1, [2,3,4] ,5]
list4=['a','b','c']

print(*list1)  #print the whole list
print(list1 , sep=" ") #print using []

list1.insert(len(list1),5) # index , value
list1.append(6)    # add it at the end of the list
list1.extend([7,8,9]) #add a list at the end of mylist

list1.pop(4)     # take an index of the number i want to remove
del list1[2]     #delete an elment using index
#itration
for i in list1:
    print(i)
#lists are mutable >values can be changed

#The challenge comes when the list gets bigger so the dictionary will be an optimized solution
employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]

def get_employee(id): 
    for employee in employee_list:
        if employee['id'] == id:
            return employee

print(get_employee(12458));
## OUTPUT
{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}