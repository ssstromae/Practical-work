for debtor in range (10):
    num = int(input("Введите число: ", ))

    if num > 0 and num % 2 == 0:
        print("Человек под номером -", debtor, "Должник")
    else:
        print("Человек под номером -", debtor, "Законопослушный гражданин")