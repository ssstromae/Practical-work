print("Начался восьмичасовой рабочий день.")

counter_hours = 0
counter_issue = 0

while counter_hours <= 7:
    counter_hours = counter_hours + 1

    print(str(counter_hours) + "-й час")

    issue = int(input("Сколько задач решит Максим?"), )

    counter_issue = counter_issue + issue

    wife = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет):"), )


print("Рабочий день закончился. Всего выполнено задач:", counter_issue)
if wife == 1:
    print("Нужно зайти в магазин.")
   

    