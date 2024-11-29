# Импортируем библиотеку статистика
import statistics
# Создаем ряд чисел Фибоначчи до N
N  = input("Введите значение:") #вводим значение с клавиатуры
N  = int(N) #присваиваем N числовое значение
fib_list = [0, 1] #создаём список с первыми значениями ряда фибоначи 

for i in range (2,N): #создаём цикл который будет выполняться до N

    fib_list.append(fib_list[-1] + fib_list[-2]) #добовляем в список сумму последнего и предпоследнего значения
# создаём преобразованный список
converted_list = [] #создаём пустой список для хранения значений 
for a in fib_list: #создаём цикл для преобразования рядя фибоначи 

    #задаём условие для чётных
    if a % 2 == 0: 
        converted_list.append(a * 2)

        # условие для нечётных
    else: 

        converted_list.append(a ** 2)

# находим миинимальный, максимальный эллемент, длинну списка, колличество эллементов больше медианного значения
min = min(converted_list)#минимальное значение
max = max(converted_list) #максимальное значение
length = len(converted_list) # длина списка
median = statistics.median(converted_list) # медианное значения
number_of_elements_is_greater_than_median = sum(1 for a in converted_list if a > median ) # Количество элементов больше медианного значения
# Выводим результаты
print("Исходный ряд Фибоначчи:",fib_list)
print("Преобразованный ряд:", converted_list)
print("Минимальное значение:", min)
print("Максимальное значение:", max)
print("Длина списка:", length)
print("Количество элементов больше медианного значения:", number_of_elements_is_greater_than_median)
