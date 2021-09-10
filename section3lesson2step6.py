# Дана строка s содержащая только символы '(', ')', '{', '}', '[' и ']', определите, является ли входная строка валидной.
# Входная строка допустима, если:
# Открытые скобки должны быть закрыты скобками того же типа.
# Открытые скобки должны быть закрыты в правильном порядке.
# Ограничения:
# 1 <= len(s) <= 104
# s содержит только такие скобки '()[]{}'.
s = list(input())
print(s)

result = True

# ()
parentheses = 0

# []
bracket = 0

# {}
brace = 0

for c in s:
    if c == '(':
        parentheses += 1
    elif c == ')':
        parentheses -= 1
    elif c == '[':
        bracket += 1
    elif c == ']':
        bracket -= 1
    elif c == '{':
        brace += 1
    elif c == '}':
        brace -= 1
    # если закрытых скобок стало больше чем открытых, результат False
    if parentheses < 0 or bracket < 0 or brace < 0:
        result = False
        break

# если открывающих и закрывающих скобок не равное количество, результат False
if arentheses != 0 or bracket != 0 or brace != 0:
    result = False
    
print(result)