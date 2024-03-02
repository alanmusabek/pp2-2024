import re

txt = "abb abbb abb"

x = re.findall(r"ab{2,3}", txt)
print(x)