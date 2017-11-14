import re

l= "Arizona 470, 501, 870. California 209, 213, 650."

m= re.findall("\d",l)

print(m)
