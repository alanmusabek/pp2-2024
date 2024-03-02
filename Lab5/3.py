import re

txt = "aabababa_adada"

x = re.findall(r'[a-z]+_[a-z]+', txt)

print(x)