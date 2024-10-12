numbers = [6, 5, 2, 8, 6, 10, 4, -6, -2]
result = []

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        result.append(numbers[i])

print("Элементы, которые больше предыдущего элемента:", result)
