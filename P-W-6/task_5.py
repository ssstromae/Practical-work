num_a = int(input("Введите начало отрезка: "), )
num_b = int(input("Введите конец отрезка: "), )
num_с = int(input("Введите шаг: "), )

for numbers in range(num_b, num_a - 1, num_с):
    option = numbers**3 + 2 * numbers**2 - 4 * numbers + 1
    
    print("В точке", numbers, "функция равна", option)
