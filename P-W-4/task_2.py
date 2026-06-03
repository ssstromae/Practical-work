name_debtor = str(input("Имя должника: "), )
amount_debt = int(input("Сумма долга: "), )

while True:
    print(name_debtor + ", ваша задолженность составляет", amount_debt, "рублей."  )
    
    contribution = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?"), )

    if amount_debt <= contribution:
        print("Отлично,", name_debtor +"! Вы погасили долг. Спасибо!")
        break
    else:
        print("Маловато,", name_debtor +". Давайте ещё раз.")

