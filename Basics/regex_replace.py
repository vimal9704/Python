import re

text="DevOps and Gen-Ai are the 2 Booming technologies"
pattern = r"Gen-Ai"

replacement = "Machine-learning"

new_text = re.sub(pattern, replacement, text)
print(new_text)