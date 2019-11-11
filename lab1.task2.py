"2.2Використання математичних формул за виконанням певних умов"
import re



re_integer = re.compile("^[+-]{0,1}\d$")



def validator(pattern, promt):

    text = input(promt)

    while not bool(pattern.match(text)):

        text = input(promt)

    return text





def int_greater_zero_validator(prompt):



    number = int(validator(re_integer, prompt))

    while number == 0:

        number = int(validator(re_integer, prompt))



    return number
a =int_greater_zero_validator('Enter a > 0:')
b =int_greater_zero_validator('Enter b > 0:')
c =int_greater_zero_validator('Enter c > 0:')
d =int_greater_zero_validator('Enter d > 0:')
if a == d :
    print('a = d')
if b == d :
    print('b = d')
if c == d:
    print('c = d ')
else :
    print(d-a,d-b,d-c)