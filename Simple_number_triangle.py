# 1. Простой числовой треугольник

rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ") # вывод числа
    # вывод пустой строки после каждой строки с числами для правильного отображения шаблона
    print(" ")
