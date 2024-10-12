numbers = []
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Пожалуйста, введите корректное число.")

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

even_count = len(even_numbers)
odd_count = len(odd_numbers)

print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")
print(f"Четные числа: {even_numbers}")
print(f"Нечетные числа: {odd_numbers}")
