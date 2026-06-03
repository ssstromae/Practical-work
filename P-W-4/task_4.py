counter_plus = 0
counter_minus = 0


while True:
    num = int(input("Введите число:"), )

    if num > 0:
        counter_plus = counter_plus + 1
    elif num < 0:
        counter_minus = counter_minus + 1
    elif num == 0:
        break


print("Кол-во положительных чисел:", counter_plus,"\nКол-во отрицательных чисел:", counter_minus)