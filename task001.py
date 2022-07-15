# 1. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

def find_number(list_of_strings, number):
    ans = False
    for i in list_of_strings:
        if str(number) in i:
            ans = True
            print(f'В элементе списка {i} присутствует число {number}')
    if ans == False:
        print(f'В списке строк нет числа {number}')


def find_number2(list_of_strings, number):
    s = ''.join(list_of_strings)
    if s.find(str(number)) > 0:
        print(f'В списке строк присутствует число {number}')
    else:
        print(f'В списке строк нет числа {number}')

new_list = ['qwerty1', 'uiop2', 'asdfg3']
n = int(input('Введите число: '))
find_number(new_list, n)
find_number2(new_list, n)
