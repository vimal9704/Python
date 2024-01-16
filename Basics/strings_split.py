text = "Python For DevOps"
words = text.split()
print(words)

arn = "aws:iam:role:arn:123456789/PythonForDevOps/Admin"
new_arn = arn.split("/")[1]
print("Role name is: ",new_arn)