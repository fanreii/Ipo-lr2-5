import math
S = float
a = float(input("Введите значение длины 1 основания: "))
b = float(input("Введите значение длины 2 основания: "))
c = float(input("Значение боковой стороны: "))
d = float(input("Значение второй боковой стороны: "))
p = (a + b + c + d) / 2
S = ((a + b)/ math.fabs(a - b)) * math.sqrt((p-a)*(p-b)*(p-a-c)*(p-a-d))
print("Площадь равна:", S)
