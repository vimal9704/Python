print("Enter number")
num = int(input())
print("The number is",num)
if num % 2 == 0 and 2 <= num <= 5:
    print("Wierd")
elif num % 2 != 0 and 6 <= num <= 20:
    print("Not Wierd")
else:
    print("Not Wierd")    