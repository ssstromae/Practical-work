for n in range(10, 100):  
    left = n // 10           
    right = n % 10          
    if n == (left * right) * 3:         
        print(n)