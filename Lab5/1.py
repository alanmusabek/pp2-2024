import re

txt = "abaabbbbbba"

x = re.findall("ab*", txt)

print(x)