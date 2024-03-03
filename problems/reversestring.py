my_str = "Hello there welcome to DevOps and Python scripting"

def len_str(my_str):
    re_str = ""
    for i in my_str:
        if i == 'a'|'e'|'i'|'o'|'u':
            re_str = i + re_str
            print(re_str)
    return re_str
    
output=len_str(my_str)
print(output)    