numbers = [1.6, 1.6, 1.6, 1.6]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))


numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после замены:", numbers)
