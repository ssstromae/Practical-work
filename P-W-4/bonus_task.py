low = 40
high = 80

while True:
    guess = (low + high) // 2
    answer = int(input("Ваше число меньше", guess, "или больше? 1/0"), )
    if answer == 1:
        high = guess - 1
    elif answer == 0:
        high = guess + 1

