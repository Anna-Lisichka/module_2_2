first = int(input('Введите любые 3 числа. Ваше первое число: '))
second = int(input('Ваше второе число: '))
third  = int(input('Ваше третье число: '))

if first == second ==  third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third :
    print(0)
