num = int(input("Введите N: "), )

summ = 0

for numbers in range(0, num):
    elem = (-1)**numbers * 1 / (2**numbers)
    summ += elem

print(summ) 