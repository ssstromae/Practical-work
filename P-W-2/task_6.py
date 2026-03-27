print("Задача 6. Игра в кубики.")

num_1 = int(input("Кубик Кости: ", ))
num_2 = int(input("Кубик владельца: ", ))

if num_1 >= num_2:
    print("Разность:", num_1 - num_2)
    print("Игрок платит")
else:
    print("Сумма:", num_1 + num_2)
    print("Владелец платит:")
print("Игра окончена")