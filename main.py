import random

# функция возведения в квадрат
def sqware_array(arr):
    for i in range(N):
        arr[i] = arr[i] * arr[i]
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

