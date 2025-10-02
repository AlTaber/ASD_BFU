import sys

def fail(error):
    print(f"Ошибка [❌]: {error}")
    sys.exit()

s = input("Введите число: ").strip()

if not s: fail("Пустой ввод")
try:
    x = int(s)
except: fail("Введенное число - не int")
if x < 1: fail("Введенное число должно быть натуральным")

res = []

for i in range(1, x + 1):
    t = i

    while t % 3 == 0:
        t //= 3
    while t % 5 == 0:
        t //= 5
    while t % 7 == 0:
        t //= 7
    if t == 1:
        res.append(i)

print(f"Результат: {' '.join(map(str, res))}")
