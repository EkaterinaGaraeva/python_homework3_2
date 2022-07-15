# 2. Напишите программу, которая определит позицию второго вхождения строки в списке
# либо сообщит, что её нет.
# Пример:
#
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def find_text(list_of_strings, s):
    count = 0
    index = 0
    for i in range(len(list_of_strings)):
        # print(f'i = {i}')
        if s == list_of_strings[i]:
            count += 1
            # print(f'count = {count}')
            if count == 2:
                index = i
    if count < 2:
        return -1
    else:
        return index


list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
s1 = "qwe"
print(f'{list1} => {find_text(list1, s1)}')

list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
s2 = "йцу"
print(f'{list2} => {find_text(list2, s2)}')

list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
s3 = "йцу"
print(f'{list3} => {find_text(list3, s3)}')

list4 = ["123", "234", 123, "567"]
s4 = "123"
print(f'{list4} => {find_text(list4, s4)}')

list5 = []
s5 = "123"
print(f'{list5} => {find_text(list5, s5)}')