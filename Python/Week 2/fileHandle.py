
file = open('test.txt', mode='r')
data =file.readline()
print(data)
file.close()
#read then close automatically and better at exception handling

with open ('test.txt',mode='r') as file:
     data =file.readline()
    
     print(data)

try:

     with open('newFile.txt','w') as file:
        file.writelines(["\nThis is a new file created!","\n next line"]) #\n for the newline
except FileNotFoundError as e:
    print("ERROR",e)

#'a' for appened 'r' addes the diffrent

 