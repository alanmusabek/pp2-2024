import re

txt = "camelCaseString"

x = re.findall(r'[A-z][a-z]*', txt)

y = '_'.join(word for word in x[0:])

print(y)