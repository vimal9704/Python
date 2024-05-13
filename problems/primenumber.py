def primeornot(param):
    for i in range(2, param):
        if (param%i)==0:
            print(param," Is not a prime number")
            break
    else:
        print(param," Is a prime number")
        
num = int(input("Enter any number greater than 2: "))
print(primeornot(num))        