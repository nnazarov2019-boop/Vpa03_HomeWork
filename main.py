import random

# функция возведения в квадрат
def sqware_array(arr):
    b = [0] * N
    for i in range(N):
        b[i] = arr[i] * arr[i]
    return b

# функция реерса массива
def reverse_array(arr):
    for i in range(N // 2):
        arr[i], arr[N - i - 1] = arr[N - i - 1], arr[i]
    return arr

print("Изучение языка Python")
N = 20 # размер массива
# создаем массив
a = [0] * N
print(a)

for i in range(N):
    # генерируем случайное число
    a[i] = random.randint(-100, 100)

print("Массив:", a)

print("Квадраты элементов массива:", sqware_array(a))
print("Реверс массива:", reverse_array(a))

