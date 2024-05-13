string = "Hello world"
vowel_str = []
for x in string:
    if x in "aeiou":
        vowel_str.append(x)
vowel_str.reverse()
for y in vowel_str:
    if y in "aeiou":
        print(y)