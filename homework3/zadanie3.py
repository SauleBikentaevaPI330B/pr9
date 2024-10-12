numbers = [] 

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    
    if user_input.lower() == "end":  
        break
  
    filtered_input = ''.join(char for char in user_input if char.isdigit() or char in ['.', '-'])
    
    if filtered_input:  
        try:
            number = float(filtered_input)  
            numbers.append(number)  
        except ValueError:
            print("Ошибка при преобразовании числа.")
    else:
        print("Пожалуйста, введите корректное число.")

odd_numbers = [num for num in numbers if (num % 2 != 0) or (isinstance(num, float) and str(num).split('.')[-1][-1] in '13579')]

print("Нечетные элементы списка:", odd_numbers)
