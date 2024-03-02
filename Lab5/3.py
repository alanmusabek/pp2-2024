import re

with open("./row.txt", "r", encoding="utf-8") as file:
    txt = file.read()

x = re.findall(r'[a-z]+_[a-z]+', txt)

print(x)