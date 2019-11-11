import re



re_integer = re.compile("^[-+]{0,1}\d+$")



def validator(pattern, promt):

    text = input(promt)

    while not bool(pattern.match(text)):

        text = input(promt)

    return text





def int_greater_zero_validator(prompt):



    number = int(validator(re_integer, prompt))

    while number<=0:

        number = int(validator(re_integer, prompt))



    return number
s = 0
n = int_greater_zero_validator('Enter n:')
x = int_greater_zero_validator('Enter x: ')
for i in range(1,n+1):
    s = s + (2 * x ** i) /(n - 1)
print(s)
print('Цикл завершено')