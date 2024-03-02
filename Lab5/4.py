import re

txt = "ABCedf"

x = re.findall(r'[A-Z][a-z]+', txt)

print(x)