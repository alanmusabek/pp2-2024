import re

txt = "adgdgegdgb"

x = re.findall(r'^a.*b$', txt)

print(x)