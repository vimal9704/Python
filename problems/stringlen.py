my_str = "Hello there welcome to DevOps and Python scripting"

def len_str(my_str):
    len_count = 0
    for i in my_str:
        len_count = len_count + 1
    return len_count
    
output=len_str(my_str)
print(output)    