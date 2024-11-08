def ifevenodd(n):
    if (n ^ 1 == n + 1):
        return True
    else:
        return False
    
number = int(input("enter your number: "))
    
if ifevenodd(number):
    print(number, 'is Even')
else:
    print(number, 'is Odd')