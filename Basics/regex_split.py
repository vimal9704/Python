import re

text = "aws:iam:role:arn:PythonForDevOps"
pattern = r":"

split_result = re.split(pattern, text)
print(split_result)