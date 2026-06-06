buckwheat = 100
month = 0

for consumption in range(buckwheat, 0, -4):
    month += 1
    print("Остаток гречки через месяц:", consumption)
    
print("Гречки хватит на -", month, "месяцев!" )