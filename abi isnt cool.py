def Sphere(a):
    return 4 * 3.14

result = Sphere(20)
print("the surface of the sphere is, ", result)

def ChangeChecker(a):
    if a % 5==0:
        print("no pennies needed")
    else:
        print("you need pennies for this!")
        
ChangeChecker(17)

def prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime
    
        
prime = prime(17)
if prime == True:
        print("the number is a prime number")
else:
        print("the number is NOT a prime number")
