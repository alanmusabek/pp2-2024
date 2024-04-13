# import re

# with open("./row.txt", "r", encoding="utf-8") as file:
#     txt = file.read()
#     print(txt)

# x = re.findall(r"ab{2,3}", txt)
# print(x)

import re
with open("./row.txt", "r", encoding="utf-8") as file:
    txt = file.read()
    print(txt)

x = re.findall(r"&a", txt)
print(x)