def ispalindrome(str):
    sindx=0
    eindx=len(str)-1
    siz =len(str)/2
    while siz>=0:
        
        if str[sindx]!=str[eindx]:
            return False
        sindx+=1
        eindx-=1
        siz -= 1
    return True

print(ispalindrome('abcba'))

#Constant >> O(c)

#Logarithmic >> O(log(n))

#Linear >> O(n)

#Quadratic >> O(n^2)

#Cubic >> O(n^3)

#Exponential >> O(2^n)

#Factorial >> O(n!)

