with open("./row.txt", "r", encoding="utf-8") as file:
    txt = file.read()

x = txt.replace(' ', ':').replace(',', ':').replace('.', ':')

print(x)