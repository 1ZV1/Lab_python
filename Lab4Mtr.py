#about strings

def swap_short_long_word(txt):
    words = txt.split()
    shortest = min(words, key=len)
    longest = max(words, key=len)

    idx_short = words.index(shortest)
    idx_long = words.index(longest)

    words[idx_short], words[idx_long] = words[idx_long], words[idx_short]

    return " ".join(words)


text = input("Input smth: ")
text = swap_short_long_word(text)
print(text)


N = int(input("Введите размер квадратной матрицы (N): "))

print(f"Введите элементы матрицы по строкам (через пробел, {N} чисел в строке):")
matrix = []

for i in range(N):
    while True:
        try:
            
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
            
            if len(row) != N:
                print(f"Ошибка! Вы должны ввести ровно {N} чисел. Попробуйте снова.")
                continue
                
            matrix.append(row)
            break
        except ValueError:
            print("Ошибка! Вводите только целые числа. Попробуйте снова.")

max_elements_in_negative_cols = []

for j in range(N):
    has_positive = False
    
    for i in range(N):
        if matrix[i][j] > 0:
            has_positive = True
            break
            
    if not has_positive:
        current_max = matrix[0][j] 
        for i in range(1, N):
            if matrix[i][j] > current_max:
                current_max = matrix[i][j]
        
        max_elements_in_negative_cols.append((j, current_max))

negative_count = 0

for i in range(N):
    for j in range(N):
        if i + j >= N - 1:
            if matrix[i][j] < 0:
                negative_count += 1

print("\nВаша матрица:")
for row in matrix:
    print(row)

print("\n1. Результаты по столбцам без положительных элементов:")
if max_elements_in_negative_cols:
    for col_idx, value in max_elements_in_negative_cols:
        print(f"   В столбце {col_idx + 1} (индекс {col_idx}) максимум: {value}")
else:
    print("   Таких столбцов нет.")

print(f"\n2. Количество отрицательных элементов в нижнем правом треугольнике: {negative_count}")

