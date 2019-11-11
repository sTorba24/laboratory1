"1.Піднесення змінної а до степеня за допомогою операції множення"

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


number = int_greater_zero_validator('Enter integer >0:')
grade = int_greater_zero_validator('Enter grade')

print(number**grade)