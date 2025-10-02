import sys

def fail(error):
    print(f"Ошибка [❌]: {error}")
    sys.exit()

s = input("Введите выражение: ").replace(" ", "")

if not s: fail("Выражение не существует")
if not s.endswith("="): fail("Нет знака '=' в конце")

expr = s[:-1]

if not expr: fail("Пустое выражение")

allowed = "0123456789+-*/()"
for ch in expr:
    if ch not in allowed: fail(f"Недопустимый символ \"{ch}\"")

stack = []
for ch in expr:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if not stack: fail("Неверное расположение скобок")
        stack.pop()
if stack: fail("Неверное расположение скобок")

prio = {'+': 1, '-': 1, '*': 2, '/': 2}

out = []
ops = []

i = 0
n = len(expr)
prev_is_val = False

while i < n:
    ch = expr[i]

    if ch.isdigit():
        if prev_is_val: fail("Пропущен оператор")
        j = i
        while j < n and expr[j].isdigit():
            j += 1
        out.append(int(expr[i:j]))
        prev_is_val = True
        i = j
        continue

    elif ch in '+-*/':
        if not prev_is_val: fail("Лишний оператор")
        while ops and ops[-1] != '(' and prio[ch] <= prio[ops[-1]]:
            out.append(ops.pop())
        ops.append(ch)
        prev_is_val = False

    elif ch == '(':
        if prev_is_val: fail("Пропущен оператор")
        ops.append('(')
        prev_is_val = False

    elif ch == ')':
        if not prev_is_val: fail("Неверное расположение скобок")
        while ops and ops[-1] != '(':
            out.append(ops.pop())
        if not ops: fail("Неверное расположение скобок")
        ops.pop()
        prev_is_val = True

    i += 1

if not prev_is_val: fail("Лишний оператор")

while ops:
    t = ops.pop()
    if t == '(': fail("Неверное расположение скобок")
    out.append(t)

stack = []

print(out)

for x in out:
    if isinstance(x, int):
        stack.append(x)
    else:
        if len(stack) < 2: fail("Неверное выражение")
        b = stack.pop()
        a = stack.pop()
        if x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '*':
            stack.append(a * b)
        elif x == '/':
            if b == 0: fail("Деление на 0")
            stack.append(a / b)

if len(stack) != 1: fail("Неверное выражение")

print(f"Результат: {stack[0]}")
