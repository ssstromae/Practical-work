print("Задача 8. Максимальное число. ")

num_1 = int(input("Введите первое число: ", ))
num_2 = int(input("Введите второе число: ", ))
num_3 = int(input("Введите третье число: ", ))

if num_1 > num_2 and num_1 > num_3:
    print("Большее число:", num_1)
else:
    if num_2 > num_1 and num_2 > num_3:
        print("Большее число:", num_2)
    else:
     print("Большее число:", num_3)   