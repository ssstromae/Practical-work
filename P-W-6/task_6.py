educational_grant = int(input("Введите стипендию: "), )
living_expenses = int(input("Введите расходы на проживание: "), )

print()

lack_count = 0

for month in range(1, 11):
    lack = living_expenses - educational_grant
    lack_count += lack
    
    print(str(month) +". месяц траты:", round(living_expenses, 2), "не хватает:", round(lack_count, 2))
    
    living_expenses = living_expenses + living_expenses * 0.03
    print()

print("Нужно попросить у родителей", round(lack_count, 2), "рублей.")