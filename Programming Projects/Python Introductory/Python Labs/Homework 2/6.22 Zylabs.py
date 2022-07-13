# Andy Luong 1525166
# Zylabs 6.22

x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())

a = 12
b = 12
for x in range(-10,11):
    for y in range(-10,11):
        eq1 = x1*x + y1*y - z1
        eq2 = x2*x + y2*y - z2
        if eq1 == eq2 and eq1 == 0:
            a = x
            b = y
if a != 12:
    print(a, b)
else:
    print("No solution")
