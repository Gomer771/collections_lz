def fibonacci_series(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def process_fibonacci(fib_series):
    processed_series = []
    for num in fib_series:
        if num % 2 == 0:
            processed_series.append(num * 2)  # Умножаем чётные элементы на два
        else:
            processed_series.append(num ** 2)  # Возводим нечётные элементы в квадрат
    return processed_series

def analyze_series(processed_series):
    min_value = min(processed_series)
    max_value = max(processed_series)
    length = len(processed_series)
    median_value = sorted(processed_series)[length // 2]  # Находим медиану
    count_above_median = sum(1 for x in processed_series if x > median_value)  # Количество элементов больше медианной

    return min_value, max_value, length, count_above_median

# Ввод значения N
N = int(input("Введите количество элементов ряда Фибоначчи (N): "))
fib_series = fibonacci_series(N)
processed_series = process_fibonacci(fib_series)
min_value, max_value, length, count_above_median = analyze_series(processed_series)

print(f"Обработанный ряд Фибоначчи: {processed_series}")
print(f"Минимальный элемент: {min_value}")
print(f"Максимальный элемент: {max_value}")
print(f"Длина списка: {length}")
print(f"Количество элементов, больших медианного значения: {count_above_median}")