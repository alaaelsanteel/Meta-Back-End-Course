current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')

current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')
     
  #elif >> else if   

#match
http_status = 200
match http_status:
    case 200 | 201:  #or
        print('Success')
    case  400:
        print('Bad Request')
    case 404:
        print('Not Found')
    case 500 |501:
        print('Server Error')
    case _:      #else
        print('Unknowen')


 #isinstance(object, classinfo) checks if the object is part of or subclass of classinfo
numbers = [1, 2, 3, 4, 2, 5]
# check if numbers is instance of list
result = isinstance(numbers, list)