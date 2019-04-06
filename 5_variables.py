########################################################################################################################

# 19 - Что такое переменная

"""
Задание:
Создайте переменную с именем motto и содержимым What Is Dead May Never Die!. Распечайте содержимое переменной
"""

# Solution:

motto = 'What Is Dead May Never Die!'
print(motto)

########################################################################################################################

# 20 - Изменение переменной

"""
Задание:
В упраженнии определена переменная внутри которой строчка. Переопределите значение этой переменной и присвойте
ей ту же строчку, но в перевернутом виде
"""

# Solution:
name = 'Brienna'

# BEGIN
name = 'anneirB'
# END

print(name)

########################################################################################################################

# 21 - Именование переменных

"""
Задание:
Создайте две переменные с именами «первое число» и «второе число» на английском языке используя snake_case
Запишите в первую переменную число 20, во вторую — -100. Выведите на экран произведение чисел, записанных
в получившиеся переменные
"""

# Solution:

first_number = 20
second_number = -100

print(first_number * second_number)

########################################################################################################################

# 22 - Ошибки при работе с переменными

"""
Задание:
Найдите в программе необъявленную переменную и объявите ее присвоив ей значение ‘Dragon'
"""

# Solution:

family = 'Targaryen'

# BEGIN
pet = 'Dragon'
# END

print(family)
print(' and ')
print(pet)

########################################################################################################################

# 23 - Выражения в определениях

"""
Задание:
Напишите программу, которая берет исходное количество евро, записанное в переменную euros, переводит евро в доллары
и выводит на экран. Затем полученное значение переводит в рубли и выводит на новой строчке

Пример вывода для 100 евро:
  125.0
  7500.0

Считаем, что:
      1 евро = 1.25 долларов
      1 доллар = 60 рублей
"""

# Solution:

euros = 100

# BEGIN
dollars = euros * 1.25
print(dollars)
rubles = dollars * 60
print(rubles)
# END

########################################################################################################################

# 24 - Переменные и конкатенация

"""
Задание:
Сайты постоянно посылают письма своим пользователям. Типичная задача — сделать автоматическую отправку персонального
письма, где в заголовке будет имя пользователя. Если где-то в базе сайта хранится имя человека в виде строки, то
задача генерации заголовка сводится к конкатенации: например, нужно склеить строку Здравствуйте со строкой, где
записано имя
Напишите программу, которая будет генерировать заголовок и тело письма, используя уже готовые переменные, и выводить
получившиеся строки на экран. Для заголовка используйте переменные first_name и greeting, запятую и восклицательный
знак. Выведите это на экран в правильном порядке
Для тела письма используйте переменные info и intro, при этом второе предложение должно быть на новой строке#
Результат на экране будет выглядеть так:

Hello, Joffrey!
Here is important information about your account security.
We couldn't verify you mother's maiden name.

Выполните задание, используя только два print
"""

# Solution:

info = "We couldn't verify you mother's maiden name."
intro = "Here is important information about your account security."

first_name = 'Joffrey'
greeting = 'Hello'

# BEGIN
print(greeting + ", " + first_name + "!")
print(intro + "\n" + info)
# END

########################################################################################################################

# 25 - Магические числа

"""
Задание:
Вы столкнулись с таким кодом, который выводит на экран общее количество комнат во владении нынешнего короля:
      king = 'King Balon the 6th'
      print(king + ' has ' + str(6 * 17) + ' rooms.')
Как видите, это магические числа: непонятно, что такое 6 и что такое 17. Можно догадаться, если знать
историю королевской семьи: каждый новый король получает в наследство все замки от предков и строит новый замок
— точную копию родительского. Эта странная династия просто плодит одинаковые замки…

Избавьтесь от магических чисел, создав новые переменные, а затем выведите текст на экран. Получится так:
      King Balon the 6th has 102 rooms.
"""

# Solution:

king = 'King Balon the 6th'

# BEGIN
rooms = 102
print(king + ' has ' + str(rooms) + ' rooms.')
# END

########################################################################################################################

# 26 - Константы

"""
Задание:
Создайте константу DRAGONS_BORN_COUNT и запишите в неё число 3 — это количество драконов, родившихся у Дайенерис
"""

# Solution:

DRAGONS_BORN_COUNT = 3

########################################################################################################################

# 27 - Интерполяция

"""
Задание:
Выведите на экран строку Do you want to eat, <name>?. Где вместо <name> должна использоваться переменная stark
"""

# Solution:

stark = 'Arya'

# BEGIN
template = "Do you want to eat, {}?"
print(template.format(stark))
# END

########################################################################################################################

# 28 - Извлечение символов из строки

"""
Задание

Вам даны три переменные с фамилиями разных людей. Составьте и выведите на экран слово из символов в таком порядке:

    третий символ из первой строки;
    второй символ из второй строки;
    четвертый символ из третьей строки;
    пятый символ из второй строки;
    третий символ из второй строки;
"""

# Solution:

one = 'Naharis'
two = 'Mormont'
three = 'Sand'

# BEGIN
print(one[2] + two[1] + three[3] + two[4] + two[2])
# END

########################################################################################################################

# 29 - Multi-line строки

"""
Задание:
Запишите в переменную text текст, который приведен ниже. Используйте тройные кавычки
  Lannister, Targaryen, Baratheon, Stark, Tyrell...
  they're all just spokes on a wheel.
  This one's on top, then that one's on top, and on and on it spins,
  crushing those on the ground.
"""

# Solution:

# BEGIN
text = """Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground."""
# END

print(text)

########################################################################################################################
