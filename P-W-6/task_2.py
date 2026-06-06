number_debtors = int(input("Введите количество должников: "), )

total = 0

for debtors in range(0, number_debtors, 5):
    print("Должник с номером ", debtors)
    
    debt = int(input("Сколько должны? "), )
    
    total += debt

print("Общая сумма долга:", total) 