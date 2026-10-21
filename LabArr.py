import random

MAX_SIZE = 100

while True:
    try:
        n = int(input(f"Введите количество элементов (от 1 до {MAX_SIZE}): "))
        if 1 <= n <= MAX_SIZE:
            break
        print("Ошибка: выход за границы допустимого размера.")
    except ValueError:
        print("Ошибка: введите целое число.")

arr = [0] * MAX_SIZE

while True:
    choice = input("Заполнить массив: 1 - с клавиатуры, 2 - случайными числами: ")
    if choice in ('1', '2'):
        break
    print("Ошибка: выберите 1 или 2.")

if choice == '1':
    print(f"Введите {n} целых чисел:")
    for i in range(n):
        while True:
            try:
                arr[i] = int(input(f"Элемент [{i}]: "))
                break
            except ValueError:
                print("Ошибка: введите целое число.")
else:
    while True:
        try:
            min_val = int(input("Введите нижнюю границу случайных чисел: "))
            max_val = int(input("Введите верхнюю границу случайных чисел: "))
            if min_val <= max_val:
                break
            print("Ошибка: нижняя граница больше верхней.")
        except ValueError:
            print("Ошибка: введите целые числа.")
            
    for i in range(n):
        arr[i] = random.randint(min_val, max_val)

print("\nИсходный массив:", arr[:n])

product = 1
for i in range(0, n, 2):
    product *= arr[i]
print(f"Произведение элементов с четными номерами: {product}")

first_zero = -1
last_zero = -1

for i in range(n):
    if arr[i] == 0:
        if first_zero == -1:
            first_zero = i
        last_zero = i

if first_zero != -1 and last_zero != -1 and first_zero != last_zero:
    sum_zeros = 0
    for i in range(first_zero + 1, last_zero):
        sum_zeros += arr[i]
    print(f"Сумма между первым и последним нулем: {sum_zeros}")
else:
    print("В массиве нет двух нулей, вычисление суммы невозможно.")

insert_pos = 0

for i in range(n):
    if arr[i] < 0:
        if i > insert_pos:
            temp = arr[i]
            for j in range(i, insert_pos, -1):
                arr[j] = arr[j - 1]
            arr[insert_pos] = temp
        
        insert_pos += 1

print("Преобразованный массив:", arr[:n])