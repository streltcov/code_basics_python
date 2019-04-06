########################################################################################################################

# 30 - Функции и их вызов

"""
Задание:
В 7 королевствах жил один человек, который имел доступ к компьютерам и умел программировать — Сэм Тарли
Он занимался картографией, поэтому он написал для себя функцию calculate_distance, высчитывающую расстояние (в лигах)
между городами. Функция принимает два строковых параметра — два названия городов, и возвращает число — расстояние
между ними.

Вот пример использования, где на экран выводится расстояние между Lannisport и Bayasabhad:

from hexlet.code_basics import calculate_distance

distance = calculate_distance('Lannisport', 'Bayasabhad')
print(distance)

Воспользуйтесь функцией calculate_distance и выведите на экран расстояние между городами Qarth
и Vaes Dothrak. Не копируйте пример, а создайте переменную с другим именем и напишите код с нуля самостоятельно
"""

# Solution:

from hexlet.code_basics import calculate_distance

# BEGIN
print(calculate_distance('Qarth', 'Vaes Dothrak'))
# END

########################################################################################################################

# 31 - Сигнатура фукнции

"""
Задание
В Python есть функция hex. Изучите её сигнатуру на странице документации.
Напишите программу, которая использует функцию hex с переменной number и выводит результат на экран

Определения

    Сигнатура функции — формальное описание типов аргументов и типа возвращаемого значения функции
"""

# Solution:

number = 255

# BEGIN
print(hex(number))
# END

########################################################################################################################

# 32 - Стандартная библиотека

"""
Задание
Функция type позволяет определить тип передаваемого аргумента. Название типа возвращается в виде строки. Например,
вызов type(10) вернет строку <class 'int'> (int, это сокращение от integer — целое число)

Выведите на экран тип значения переменной motto
"""

# Solution:

motto = 'Family, Duty, Honor'

# BEGIN
print(type(motto))
# END

########################################################################################################################

# 33 - Аргументы по умолчанию

"""
Задание
Округлите число, записанное в переменную number, до двух знаков после запятой и выведите результат на экран
"""

# Soluton:

number = 10.1234

# BEGIN
print(round(number, 2))
# END

########################################################################################################################

# 34 - Вызов функции - выражение

"""
Задание
Арья собирается в путешествие из Винтерфела в Орлиное гнездо, чтобы навестить Лизу Аррен, но по пути ей нужно заехать
к Фреям для совершения акта возмездия. Ей нужно рассчитать общую длину маршрута

К сожалению, функция calculate_distance может вычислять расстояние только между двумя точками. Поэтому придется
сначала узнать расстояние от Винтерфелла до замка Фреев, а потом расстояние до Орлиного гнезда

Названия замков на английском языке:

    Винтерфелл — Winterfell
    Близнецы (Замок Фреев) — The Twins
    Орлиное гнездо — The Eyrie

Выведите на экран полную длину маршрута Арьи. Напомним, что функция calculate_distance принимает два аргумента
и возвращает число
"""

# Solution:

from hexlet.code_basics import calculate_distance

# BEGIN
print(calculate_distance('Winterfell', 'The Twins') + calculate_distance('The Twins', 'The Eyrie'))
# END

########################################################################################################################

# 35 - Аргументы как выражения

"""
Задание
Вам доступна функция calculate_distance_between_towns. Она принимает один аргумент, в котором должны содержаться
названия двух городов через дефис. В ответ она возвращает расстояние между этими городами. Вот пример использования:
      distance = calculate_distance_between_towns('Lannisport-Bayasabhad')

Напишите программу, которая использует функцию calculate_distance_between_towns и выводит на экран расстояние
между городами, записанными в переменные source и destination
"""

# Solution:

from hexlet.code_basics import calculate_distance_between_towns

source = 'The Twins'
destination = 'The Eyrie'

# BEGIN
print(calculate_distance_between_towns(source + '-' + destination))
# END

########################################################################################################################

# 36 - Вызов функций в аргументах функций

"""
Задание
Для построения генеалогического дерева семьи Старков Сэм написал функцию parent_for, которая возвращает имя родителя,
если передать ей первым параметром имя ребенка. Вторым параметром функция принимает строчку 'father' или 'mother'
Так функция понимает, кого из родителей возвращать. По умолчанию параметр равен 'mother'. То есть, если нужно узнать
имя матери, то можно не передавать специально 'mother', а передать лишь один параметр — имя ребенка

Напишите программу, которая выводит на экран имя деда Джоффри по материнской линии. Полное имя Джоффри на
английском: 'Joffrey Baratheon'
"""

# Solution:

from hexlet.code_basics import parent_for

# BEGIN
print(parent_for(parent_for('Joffrey Baratheon'), 'father'))
# END

########################################################################################################################

# 37 -Побочные эффекты

"""
Задание
Это задание не связано напрямую с уроком. Но выполнить его без создания переменных — важный шаг в вашем
профессиональном развитии
Выведите на экран имя матери Дайнерис Таргариен (Daenerys Targaryen), используя функцию parent_for без создания
переменных
Напомним, что parent_for принимает первым параметром имя ребенка и возвращает имя родителя. Вторым параметром функция
принимает строчку 'father' или 'mother'. Так функция понимает, кого из родителей возвращать. По умолчанию параметр
равен 'mother'
"""

# Solution:

from hexlet.code_basics import parent_for

# BEGIN
print(parent_for('Daenerys Targaryen'))
# END

########################################################################################################################

# 38 - Неизменяемость и примитивные типы

"""
Задание
Переведите число, записанное в переменную value, в шестнадцатиричный вид, используя функцию hex. Новое значение (а
это уже будет строка!) запишите в ту же переменную value

Возможно, вам покажется, что код получился странным. Это типичный пример: переписывание переменных делает код
менее понятным и более запутанным, особенно в таких случаях, как этот - когда новое значение имеет тип, отличающийся
от типа старого значения
"""

# Solution:

value = 42

# BEGIN
value = hex(value)
# END

print(value)

########################################################################################################################
