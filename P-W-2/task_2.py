print("Задача 2. Поступление.")

russ_scores = int(input("Введите количество баллов по русскому языку: ", ))
math_scores = int(input("Введите количество баллов по математике: ", ))
computer_science_scores = int(input("Введите количество баллов по информатике: ", ))
entrance_score = 265

if (russ_scores + math_scores + computer_science_scores) >= entrance_score:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")