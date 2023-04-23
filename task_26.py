# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов.

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

print()
print(('Значение факториала N! - '),factorial(int(input('Введите значение N - '))))

def tri_Number(n):
    if(n == 1):
        return 1
    else:
        return tri_Number(n-1)+n
    
print()
print(('Значение триугольного числа - '),tri_Number(int(input('Введите значение N - '))))   
print()
