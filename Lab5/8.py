import re
with open("./row.txt", "r", encoding="utf-8") as file:
    txt = file.read()

x = re.findall(r'[A-z][a-z]*', txt)

print(x)