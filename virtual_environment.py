# import pandas as pd
# print(pd.__version__)


# how to import works in python

# import pandas
# pandas.read_csv()

# import math
# math.floor(4.2343)

# import math
# from unittest import result

# result = math.sqrt(9)
# print(result)

from math import pi, sqrt
result = sqrt(9) * pi
print(result)

# OR,

from math import *
result = sqrt(9) * pi
print(result)

from math import pi, sqrt as s
import math as m
result = s(9) * pi
print(result)


import math as m
result = m.sqrt(9) * m.pi
print(result)

import math as math_builtin_python
result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)

# to see what are the function and veriable in math .
import math

print(dir(math))
print(math.nan, type(math.nan))

# from another folder to this we can import the function like this , here i have import  from function.py folder
from function import * # in case of * we can use name, average, etc...
function()
print(name)

