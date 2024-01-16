import re

text = "The quick brown fox"
pattern = r"quick"

#match checks for patter at the beginning of the string
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")