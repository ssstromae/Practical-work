students = int(input("Учеников в классе: "), )


excellent_count = 0
good_count = 0
satisfactory = 0


for i in range(students):
    score = int(input("Какую оценку получил ученик? "), )
    if score == 5:
        excellent_count += 1
    elif score == 4:
        good_count += 1
    elif score == 3:
        satisfactory += 1



if excellent_count < good_count > satisfactory:
    print("Больше хорошистов!")
elif   good_count < excellent_count > satisfactory:
    print("Больше отличноиков!")
elif good_count < satisfactory > excellent_count:
    print("Больше троечников!")
