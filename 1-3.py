
x = float(input ("введите первое число: "))
y = float(input ("введите второе число: "))

max = (x > y) * x + (y > x) * y
print(max)