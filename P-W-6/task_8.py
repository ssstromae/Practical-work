boys = int(input("Введите количество мальчиков: "), )
girls = int(input("Введите количество девочек: "), )

if boys > girls * 2 or girls > boys * 2:
    print("Нет решения.")
else:
    result = ""
    if boys >= girls:
        result += "BG"
        boys -= 1
        girls -= 1
        while girls > 0:
             if boys > girls:
                result += "BBG"
                boys -= 2
                girls -= 1
             else:
                result += "BG"
                boys -= 1
                girls -= 1
        result += "B" * boys
    
    else:
        result += "GB"
        boys -= 1
        girls -= 1
        while boys > 0:
             if girls > boys:
                result += "GGB"
                boys -= 1
                girls -= 2
             else:
                result += "GB"
                boys -= 1
                girls -= 1
        result += "G" * girls

    print(result)