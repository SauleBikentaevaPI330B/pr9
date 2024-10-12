import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def user_selection():
    user_numbers = []
    for i in range(len(ticket)):
        while True:
            try:
                number = int(input(f"Выберите число из строки {i + 1} {ticket[i]}: "))
                if number in ticket[i]:
                    user_numbers.append(number)
                    break
                else:
                    print("Число не в строке. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")
    return user_numbers

def random_selection():
    random_numbers = []
    for row in ticket:
        random_numbers.append(random.choice(row))
    return random_numbers

def count_matches(user_numbers, random_numbers):
    return len(set(user_numbers) & set(random_numbers))

user_numbers = user_selection()
random_numbers = random_selection()

print(f"\nВаши числа: {user_numbers}")
print(f"Случайно выбранные числа: {random_numbers}")

matches = count_matches(user_numbers, random_numbers)
print(f"Количество совпадений: {matches}")
