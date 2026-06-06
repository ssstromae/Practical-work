num_a = int(input("Введите первое число: "), )
num_b = int(input("Введите второе число: "), )
num_с = int(input("Какому числу кратны: "), )

count_a = 0
count_b = 0


for numbers in range(num_a, num_b + 1):
    if numbers%num_с == 0:
        count_a += 1
        count_b += numbers
    
    

print("Среднее арифметическое всех чисел из отрезка [", num_a, ";", num_b, "], кратные числу",num_с,":", count_b // count_a)