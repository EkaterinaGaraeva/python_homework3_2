# 3* (необзательная).
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов
# и в каком количестве используется в этой книге.
#
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
# разделённые пробелом и вывести получившуюся статистику.
#
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального
# слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.
#
# Sample Input 1:
#
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2
#
# Sample Input 2:
# a A a
# Sample Output 2:
# a 3

def word_count(line_of_text):
    list_of_words = line_of_text.lower().split()
    dictionary_of_words = {}
    for word in list_of_words:
        if word not in dictionary_of_words.keys():
            dictionary_of_words[word] = 1
        elif word in dictionary_of_words.keys():
            dictionary_of_words[word] += 1
    return dictionary_of_words


s = input('Введите текст: ')
d = word_count(s)
for word, count in d.items():
    print(word, count)

s2 = 'a aa abC aa ac abc bcd a'
print('\n' + s2)
d2 = word_count(s2)
for word2, count2 in d2.items():
    print(word2, count2)

s3 = 'a A a'
print('\n' + s3)
d3 = word_count(s3)
for word3, count3 in d3.items():
    print(word3, count3)