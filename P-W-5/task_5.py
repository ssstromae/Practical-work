num_1 = int(input("Введите первое число: "), )
num_2 = int(input("Введите второе число: "), )

total_1 = 0
total_2 = 0

for i in range(num_1, num_2 + 1):
    if i % 3 == 0:
        total_1 += 1 
        total_2 += i
        average = total_2 / total_1
    
print("Среднее арифметическое равно:", average)  
