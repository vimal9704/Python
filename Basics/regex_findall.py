import re

text = "Devops is not just about CICD it also covers infra creation, scripting, developing, managing cloud services"
pattern = r"CICD"

search = re.search(pattern, text)
if search:
    print("Match found:", search.group())
else:
    print("Match not found")