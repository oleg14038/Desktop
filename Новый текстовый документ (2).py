#ПОРЯДОК ВЫПОЛНЕНИЯ ПРОГРАММЫ
# Булевы значения

#Челочисленные, вещественные и строковые переменные могут иметь
#неограниченное количество значений, в то время как булев тип данных
#предполагает всего два возможных значения: True (истина) и False (ложь).

spam = True 
print(spam)

#Операторы сравнения
#Оператор Операция
#== Равно
#1 - Не равно
#< Меньше
#> Больше
#<= Меньше или равно
#>= Больше или равно

#42 == 42 ->: True 
#42 == 92 ->: False
#2 !=35 ->: True 
#2 != 2 False 


#»> 'привет' == 'привет'
#True
#>>> 'привет' == 'Привет'
#False
#»> 'собака' ’ = 'кот'
#True
#>>> True == True
#True
#»> True != False
#True
#»> 42 == 42.0
#True
# »> 42 = '42'
#False

#»> 42 < 100
#True
#»> 42 > 100
#False
#»> 42 < 42
#False
#»> eggCount = 42
#>» eggCount <= 42
#True

# Бинарные булевы операторы

#Выражение Результат
#True and True True
#True and False False
#False and True False
#False and False False


#Оператор or возвращает True, когда любой из булевых операндов равен
#True; в противном случае результат равен False
#>>> False or True
#True
#>» False or False
#False

#Таблица 2.3. Таблица истинности для оператора or

#Выражение Результат
#True or True True
#True or False True
#False or True True
#False or False False


#Оператор not
#В отличие от операторов and и or, оператор not применяется только к
#одному булевому значению (выражению), поэтому его называют унарным.
#Он возвращает значение, противоположное значению операнда.

#>>> not True
#False
#>>> not not not True
#True

#Выражение Результат
#not True False
#not False True

#(4 < 5) and (5 < 6)
#True 
#(4 < 5) and (9  <6) 
#False
#(1 == 2) or (2 == 2)
#True 

#»> 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
#True

name = 'Мэри'
password = 'Рыба-Меч'
if name == 'Мэри':
    print(f"Привет, {name}")
    if password == 'Рыба-Мечь': 
        print('Доступ разрешен ')
    else:
        print('Неверный пароль ')

# Инструкция if
# Самая распространенная управляющая инструкция — if. Вложенный
# блок кода будет выполняться только в том случае, если условие равно True
# (т.е. истинно). Если же условие равно False (т.е. ложно), то блок выполняться не будет

if name == "Alice":
    print("Hi Alice")


# Инструкция else

# Инструкция if может дополняться необязательной инструкцией else
# со своим блоком кода, который выполняется лишь в том случае, если условие if ложно
if name == "Alice":
    print("Hi Aliece")
else:
    print('Hello, stranger ')

#Инструкция elif
#Из двух блоков кода, связанных с инструкциями if и else, всегда выполняется только один. Но иногда в программе требуется проверить несколько
#условий, для каждого из которых предусмотрен свой блок кода. Инструкция elif (сокращение от “else if’) может стоять только после инструкции
#if или другой инструкции elif. Она предоставляет еще одно условие, которое проверяется лишь в том случае, если все предыдущие условия оказались ложными. В Python инструкция elif всегда состоит из следующих
#элементов:
name = 'Alice'
age1 = 30
if name == 'Alice':
    print("Hi Alice")
elif age1 < 12:
    print('You are not Alice, kido. ')
# Блок elif выполняется, если выражение аде < 12 истинно, а выражение name == ’Alice ’ ложно.

name = 'Corol'
age = 3000
if name == 'Alice': 
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kido ')
elif age > 1000:
    print("Unike you, Alice is not unded, import vampure")
elif age > 100: 
    print('You are not ALICE, grannnie ')


# Цикл while
# Инструкция while позволяет организовать многократное выполнение
# блока кода. Тело цикла while выполняется до тех пор, пока истинно заданное условие.

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

name1 = ''
while name != 'yor name ':
    print("Please type you name ")
    name = input()
print("Thank you ! ")

# Инструкция break
#Существует простой способ заставить программу досрочно выйти из
# цикла while
while True: 
    print('Plese type your name')
    name = input()
    if name == 'your name ':# Инструкция if проверяет равно ли значение переменной name строку your name 
        break
print("Thank you")

#Рассмотрим программу, которая запрашивает ввод имени пользователя и пароля
while True: 
    print('Who are you ?')
    name3 = input('Введите ИМЯ')
    if name3 != 'Joe':
        continue # Инструкция continue если name if name не равен 'Joe' то инструкция передаеться в начала цикла 
    print("Helli,Joe. What is the password ? (It is a fish)")
    password = input()
    if password == '18.05.93':
        break
print('Acces granted. ')

# Цикл for и функция range()
# Цикл while  выполняется до тех пор, пока условие остается истинным.
print('My name is')
for i in range (5):
    print(i)

# Примечание
# В циклах for тоже допускается использование инструкций break и continue.
# Инструкция continue возвращает управление в начало цикла для выполнения следующей итерации, при этом счетчик цикла увеличивается, как если бы
# программа достигла конца цикла и вернулась к его началу обычным способом.
# Порядок выполнения программы 87
# Инструкции continue и break поддерживаются только в циклах while и for.
# Если попытаться использовать их где-то еще, Python выдаст сообщение об ошибке.

total = 0 
for num in range(101):
    total = total + num 
print(total)

# Эквивалентный цикл while
print('My name is ?')
i = 0 
while i < 5: 
    print(f"Jimmy Five Times {i}")
    i = i + 1

# Аргументы начала, конца и шага функции range ()
for i in range(12, 16):
    print(i)
#12
#13
#14
#15

for i in range(0, 10, 2):#Вызов range (0, 10, 2) обеспечивает изменение счетчика цикла от 0 до 8 с шагом 2.
    print(i)
#0
#2
#4
#6
#8

# Функция range() очень гибкая в отношении форматирования последовательностей целых чисел для циклов for
# Например, можно задать отрицательный шаг, сделать так, чтобы отсчет шел от больщих значениий к меньшим 

for i in range(5, -1, -1):
    print(i)
#5
#4
#3
#2
#1
#0


# Импорт модулей
import random #Ключевое слово import, модуль random
for i in range(5):
    print(random.randint(1, 10))

#1
#8
#5
#6
#3

# Альтернативная форма import - from random import
# Досрочное завершение программы c помощью функции sys.exit()

import sys

while True: 
    print('Введите "exit" для выхода. ')
    response = input()
    if response == 'exit':
        sys.exit()
    print("Вы ввели", response,  ".")

# Короткая программа: угадай число

import random 
secretNamber = random.randint(1, 20)# функцию random, randint () для генерации числа, которое должен угадать пользовать
print("Я загадал число от 1 до 20 ")

for qussesTaken in range(1, 7):# Игроку дается 6 попыток
    print("Угадай число ")
    quess = int(input())

    if quess < secretNamber : 
        print('Число больше ')
    elif quess > secretNamber : 
        print("Число меньше ")
    else:
        break # Число угадал 

if quess == secretNamber: 
    print("Отлично,=! Вы угадали.  Количество попыток", (str(qussesTaken)),".")
else: 
    print('Вы неугадали. Я загадал число', (str(quss)), '.')



 # Короткая программа: камень, ножницы, бумага
import random, sys

print('Камень, Ножницы, Бумага')

#В этих переменных накапливается количкство 
# Побед, поражений и ничьих 

wins = 0 
losses = 0 
ties = 0 

while True:# главный цикл игры
    print('%sпобед, %sпоражений, %sничьих' %(wins, losses, ties))

    while True:
        print('Выберите ход: (к)амень, (н)ожнецы,' '(б)умага или' \
            '(в)ыход')
    playerMove = input()
    if playerMove == 'в':
        sys.exit() #выход из программы 
    if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
        break #ВЫХОД ИЗ ЦИКЛА ВЫБОРА ХОДА 
    print('Введите "к", "н", "б" или "в" ')

# Отображение выбора пользователя
if playerMove == 'к':
    print('Камень....')
elif playerMove == 'н':
    print('Ножницы....')
elif playerMove == 'б':
    print('БУМАГА и ...')  

# Отображение выбора компьютера
гandomNumber = random.randint(1, 3)
if randomNuber == 1:
    computerMove = 'к'
    print("Камень")
if randomNuber == 2: 
    computerMove = 'н'
    print('Ножницы ')
elif randomNumber == 3:
    computerMove = '6'
    print('БУМАГА')


