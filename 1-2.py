
v = int(input('введите скорость:'))
t = int(input("введите время:"))
s = v * t
s1 = ((v * t) % 109)
if s < 109:
	print(s)
else:
	print(s1)
