with open("./row.txt", "r", encoding="utf-8") as file:
    txt = file.read()

x = txt.split('_')

y = x[0] + ''.join(word.capitalize() for word in x[1:])

print(x)
