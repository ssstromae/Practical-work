print("Задача 7. Хватит ли зарплаты.")

hours = int(input("Введите отработанные часы: ", ))
credit = int(input("Введите остаток по кредиту: ", ))
money_for_food = int(input("Введите траты на еду: ", ))
salary = (200 * hours) / 2**3 + hours

if salary >= credit + money_for_food:
    print("Часов хватает. Можно отдохнуть.")
else:
    print("Часов не хватает. Придётся работать больше!")