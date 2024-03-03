def natural_number(n):
    result = n * (n+1)
    result = result / 2
    return result

n = float(input("Enter any number to find sum"))

print(natural_number(n))