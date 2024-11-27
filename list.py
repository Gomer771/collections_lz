# Функция для генерации ряда Фибоначчи до n-го элемента
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Функция для обработки списка: умножаем четные элементы на 2, нечетные возводим в квадрат
def modify_fibonacci(fib_list):
    modified_list = []
    for num in fib_list:
        if num % 2 == 0:  # Если число четное
            modified_list.append(num * 2)
        else:  # Если число нечетное
            modified_list.append(num ** 2)
    return modified_list

# Функция для анализа списка: находим минимальный, максимальный элементы, длину и количество элементов больше медианного значения
def analyze_list(modified_list):
    minimum = min(modified_list)  # Минимальный элемент
    maximum = max(modified_list)  # Максимальный элемент
    length = len(modified_list)  # Длина списка
    median = sorted(modified_list)[length // 2]  # Находим медиану
    median = sum(1 for x in modified_list if x > median)  # Количество элементов больше медианы
    
    return minimum, maximum, length, median

# Основная часть программы
n = int(input("Введите значение N: "))  # Запрашиваем у пользователя значение N
fib_list = fibonacci(n)  # Генерируем ряд Фибоначчи
modified_list = modify_fibonacci(fib_list)  # Модифицируем список
results = analyze_list(modified_list)  # Анализируем обработанный список

# Вывод результатов
print("Ряд Фибоначчи: {fib_list}")
print("Обработанный список: {modified_list}")
print("Минимальный элемент: {results[0]}")
print("Максимальный элемент: {results[1]}")
print("Длина списка: {results[2]}")
print("Количество элементов больше медианного значения: {results[3]}")