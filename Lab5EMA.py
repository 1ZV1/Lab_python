while True:
    try:
        user_input = input("Введите элементы массива через пробел: ")
        arr = [int(x) for x in user_input.split()]
        
        if not arr:
            print("Массив пуст. Пожалуйста, введите числа.")
            continue
        break
    except ValueError:
        print("Ошибка! Вводите только целые числа через пробел.")

mul = 1
for i in range(0, len(arr), 2):
    mul *= arr[i]

sum_between_zeros = 0
if arr.count(0) >= 2:
    first_zero = arr.index(0)
    last_zero = len(arr) - 1 - arr[::-1].index(0)

    sum_between_zeros = sum(arr[first_zero + 1 : last_zero])
else:
    print("\nВ массиве меньше двух нулей, вычисление суммы невозможно.")

negatives = [x for x in arr if x < 0]
others = [x for x in arr if x >= 0]
transformed_arr = negatives + others

print("\n--- Результаты ---")
print(f"Произведение элементов с четными номерами: {mul}")
if arr.count(0) >= 2:
    print(f"Сумма между первым и последним нулем: {sum_between_zeros}")
print(f"Преобразованный массив: {transformed_arr}")

