
x = int(input ("введите первое число: "))
y = int(input ("введите второе число: "))
z = int(input ("введите третье число: "))
q = (x == y) + (y == z) + (x == z)
if q >= 2:
    print(3)
elif q >= 1:
        print(2)
else:
        print(0)