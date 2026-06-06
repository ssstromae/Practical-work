reverse_timer = int(input("Время готовки еды: "), )

for timer in range(reverse_timer, -1, -1):
    print("До готовки", timer, "секунды!")
    if timer == 0:
        print("Ваша еда готова, осторожно горячo!")
        break
    continue_stop = int(input("Остановить разогрев? "), )
    if continue_stop == 1:
        print("Ваша еда готова, можете забрать")
        print("Таймер был прерван на", timer, "секунде.")
        break
    


    