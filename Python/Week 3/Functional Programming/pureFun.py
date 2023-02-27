#doesn't change the globel variables
global_list =[1,2,3]

def add_to(item):
    return global_list.append(item)  # change a global list not pure

#to make it pure 

n1= global_list.copy()

def add_to_list(global_list,item):
    n1= global_list.copy()
    n1.append(item)
    return n1
    
print(add_to_list(global_list,5))
#known output, consistent and reliable, cache, multi threaded programs

