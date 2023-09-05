def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


numbers = [7, 2, 9, 4, 1]
sort_list_imperative (numbers)
print(numbers)