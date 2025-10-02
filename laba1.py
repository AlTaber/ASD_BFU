import sys

success = "Строка существует [✅]"
fail = "Строка не существует [❌]"

s = input("Введите строку: ")

if not s:
    print(fail)
    sys.exit()

opens = "([{"
closes = ")]}"
pairs = {')': '(', ']': '[', '}': '{'}

for ch in s:
    if ch not in opens + closes:
        print(fail)
        sys.exit()

stack = []
ok = True

for ch in s:
    if ch in opens:
        stack.append(ch)
    else:
        if not stack:
            ok = False
            break
        x = stack.pop()
        if x != pairs[ch]:
            ok = False
            break

if ok and not stack:
    print(success)
else:
    print(fail)
    