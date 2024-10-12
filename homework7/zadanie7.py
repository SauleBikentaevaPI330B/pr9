numbers = [1, 2, 3, 4, 5]  

print("Исходный список:", numbers)

for _ in range(len(numbers)):
    last_element = numbers[-1] 
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1] 
    numbers[0] = last_element
    print("Список после сдвига:", numbers)
