import math
x = float(input("Введіть x\n"))
if x<=3 :
    y = -x**2-1.1*x+9
if x>3  :
    y = math.log1p(x+3)/x**2+9
print(y)
