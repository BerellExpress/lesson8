first = int(input('Введите первое число: ', ))
second = int(input('Введите второе число: ', ))
third = int(input('Введите третье число: ', ))
if first == second == third:
    print('Совпадений: ', 3)
elif first == second or first == third or second == third:
    print('Совпадений: ', 2)
elif first != second != third:
    print('Совпадений: ', 0)