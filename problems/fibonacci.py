def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n -2) + fibo(n -1)
    
n = int(input("Enter any number to get fibonacci series:"))

for i in range(0,n):
    print(fibo(i))
