import math
# print(dir(math))
print(math.pi)
print(math.e)
print(math.floor(3.999))
print(math.ceil(3.999))
print(math.pow(3,2))

# VErsion 2 for creating alias

import math as m  
print(m.pi)


# Once created alias you can not use math
print(math.floor(3.9))

# You can import math function
from math import sqrt,pi # or from math import * for all attributes

print(sqrt(16))

print(pi) # This will show as not defined as this was not called above as part of math module

# but to use above function as well you can call pi 

from math import sqrt as s, pi as p 
print(s(9))
print(p)



