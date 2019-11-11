s=0
while True:
n = int(input("Enter n: "))
x = int(input("Enter x: "))
for i in range(1,n+1):
     s = s + (2 * x ** i) /(n - 1)
print(s)
print("Цикл завершено")

