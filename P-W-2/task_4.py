print("Задача 4. Калькулятор скидки.")

item_1 = int(input("Стоимость товара: ", ))
item_2 = int(input("Стоимость товара: ", )) 
item_3 = int(input("Стоимость товара: ", ))  
cheque = item_1 + item_2 + item_3

if cheque >= 10000:
    discount = cheque * 10 / 100
    cheque = int(cheque - discount)
print("Итог:", cheque)