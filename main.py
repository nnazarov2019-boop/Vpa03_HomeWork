import random

print("Изучение языка Python")
N = 20 # размер массива
# создаем массив
a = [0] * N
print(a)

for i in range(N):
    # генерируем случайное число
    a[i] = random.randint(-100, 100)

print("Массив:", a)
