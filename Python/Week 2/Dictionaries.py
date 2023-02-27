my_d ={1 : 'coffee', 'Name':'alaa'} #key = value
my_d[2]='student'  #adding new key and value or updating a value

del my_d[2]
#print(my_d[2])
#itration
for i in my_d:  #print the keys only
    print(i)  

for key,value in my_d.items():
    print(str(key) +" "+ value)  #I'm dealing with both int and str 
    
# for larger data
    employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id];


print(get_employee_from_dict(12458));
## OUTPUT
{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}