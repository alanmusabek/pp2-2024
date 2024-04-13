import re

with open("./row.txt", "r", encoding="utf-8") as file:
    txt = file.read()

x = re.findall(r'[A-Z][a-z]+', "Biolab, Missisipi, BMW, LamborGini")

print(x)