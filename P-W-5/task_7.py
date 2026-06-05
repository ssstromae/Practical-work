card = int(input("Введите количество карточек:"), )

total = 0

for i in range(1, card + 1):
    total += i   

for i in range(1, card):
    lost_card = int(input("Введите номер оставшейся карточки:"), )
    total -= lost_card

print("Номер пропавшей карточки:", total)