# Reverse pyramid, all elements of which are represented by the same number
# Обратная пирамида, все элементы которой представлены одним и тем же числом


rows = 5
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print('\r')
