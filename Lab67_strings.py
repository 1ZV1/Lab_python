def solve_string_task():
    s = input("Введите строку (до 300 символов): ")
    if len(s) > 300:
        print("Ошибка: длина строки превышает 300 символов.")
        return

    delimiters = input("Введите символы-разделители (например, пробелы и знаки препинания): ")
    if not delimiters:
        delimiters = " "

    words = []
    separators = []
    
    current_word = []
    current_sep = []
    
    is_sep = True
    
    leading_sep = []

    i = 0
    while i < len(s):
        char = s[i]
        is_delimiter = char in delimiters
        
        if is_sep:
            if is_delimiter:
                leading_sep.append(char)
                i += 1
            else:
                is_sep = False
        else:
            if is_delimiter:
                words.append("".join(current_word))
                current_word = []
                current_sep.append(char)
                is_sep = True
                i += 1
            else:
                current_word.append(char)
                i += 1

    if current_word:
        words.append("".join(current_word))
    
    trailing_sep = []
    if is_sep and current_sep:
        trailing_sep = current_sep

    if len(words) < 2:
        print("Ошибка: строка должна состоять не менее чем из двух слов.")
        return

    max_len = -1
    first_longest_idx = -1
    for idx, w in enumerate(words):
        if len(w) > max_len:
            max_len = len(w)
            first_longest_idx = idx

    min_len = float('inf')
    last_shortest_idx = -1
    for idx, w in enumerate(words):
        if len(w) <= min_len:
            min_len = len(w)
            last_shortest_idx = idx

    words[first_longest_idx], words[last_shortest_idx] = words[last_shortest_idx], words[first_longest_idx]

    result_parts = ["".join(leading_sep)]
    for idx in range(len(words)):
        result_parts.append(words[idx])
        if idx < len(current_sep):
            result_parts.append(current_sep[idx])
        elif idx < len(words) - 1:
            result_parts.append(" ")

    if trailing_sep:
        result_parts.append("".join(trailing_sep))

    final_string = "".join(result_parts)

    print("\n--- Результат ---")
    print("Исходная строка:    ", s)
    print("Преобразованная строка:", final_string)

solve_string_task()