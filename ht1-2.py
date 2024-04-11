
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

if ((x1 == x2) & (y1 == y2)) | (x1 > 8) | (x2 > 8) | (y1 > 8) | (y2 > 8) | (x1 < 0) | (x2 < 0) | (y1 < 0) | (y2 < 0):
    print("неверные значения")
elif (x1 == x2) | (y1 == y2):
    print("YES")
else:
    print("NO")