import math

def check_uniq_digits(n: int) -> bool:
    n = abs(n)
    flag = 0

    while n > 0:
        digit = n % 10
        if flag & (1 << digit):
            return False
        flag |= (1 << digit)
        n //= 10
    return True

def check_num_Armstrong(n: int) -> bool:
    if n < 0:
        return False
        
    digits = []
    n_copy = n

    while n > 0:
        digits.append(n % 10)
        n //= 10

    power = len(digits)
    res = sum(d ** power for d in digits)
    
    return res == n_copy


num = int(input("Please, input natural number: "))

if(check_uniq_digits(num)):
    print("Different")
else:
    print("Same")

if(check_num_Armstrong(num)):
    print("Yes, it is.")
else:
    print("Not num Armstrong")