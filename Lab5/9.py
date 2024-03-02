import re

txt = "CapitalWordHelloWorld"

x = re.findall(r'[A-z][a-z]*', txt)

y = ' '.join(word for word in x[0:])

print(y)