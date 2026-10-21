import math

epsilon = 0.00000000000001
#int(input(epsilon))
x = 3

def exp_x_teilor(x: int, eps: float) -> float:
    summ = 0.0
    i = 0
    
    while True:
        elem = (x ** i) / math.factorial(i)
        
        if elem < eps:
            return summ
        
        summ += elem
        i += 1

def sin_x_teilor(x:int, eps: float)-> float:
    summ = 0.0
    i = 1
    j = 0
    while True:
        elem = ((-1)**j)*(x**i)/math.factorial(i)
        if math.fabs(elem) < eps:
            return summ
        summ += elem
        i += 2
        j += 1

print("Результат через Тейлора:", exp_x_teilor(x, epsilon))
print("Эталонный результат math.exp:", math.exp(x))
print("Результат через Тейлора:", sin_x_teilor(x, epsilon))
print("Эталонный результат math.sin:", math.sin(x))
