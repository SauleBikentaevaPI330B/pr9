while True:
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        
        start = int(min(a, b)) + 1  
        end = int(max(a, b)) - 1    

        if start > end:
            print("Нет целых чисел между a и b. Попробуйте снова.")
            continue

        squares = [i**2 for i in range(start, end + 1)]

        print("Список квадратов целых чисел между a и b:", squares)
    except ValueError:
        print("Пожалуйста, введите корректные числа.")
