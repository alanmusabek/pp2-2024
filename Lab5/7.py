txt = "sdsdsgd_egasgds_agasfga_ba"

x = txt.split('_')

y = x[0] + ''.join(word.capitalize() for word in x[1:])

print(x)
