def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Определяем целочисленный массив и искомое число
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 0

# Вызываем функцию binary_search и сохраняем результат в переменную result
result = binary_search(array, target)

# Проверяем результат
if result != -1:
    print("Элемент найден на позиции:", result)
else:
    print("Элемент не найден.")
