"""2.Дано ціле число N(&gt;1).Вивести найбільше значення із цілих
чисел K , для яких сума 1+2+…+К буде менше або дорівнює N , і
саму цю суму."""

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

n = int_greater_zero_validator("Введіть значення N(N>1)\n")
k = 0
s=0
while n>=s:
    s=s+k
    k=k+1
print(s,k)
print('Цикл завершено')
