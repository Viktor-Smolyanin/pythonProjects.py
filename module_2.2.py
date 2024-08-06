first = input('Введите число: ')
second = input('Введите число: ')
third = input('Введите число: ')
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second or second != third or first != third:
    print(0)