def quicksort(arr):
    # Базовый случай: массив из 0 или 1 элемента уже отсортирован
    if len(arr) <= 1:
        return arr
    # Выбираем опорный элемент (pivot) — возьмем средний
    pivot = arr[len(arr) // 2]
    # Делим массив на три части
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Рекурсивно сортируем левую и правую части, объединяем результат
    return quicksort(left) + middle + quicksort(right)
# Пример использования:
numbers = [3, 0, 6, -2, -6, 11, 3]
print(quicksort(numbers))
# Вывод: [-6, -2, 0, 3, 3, 6, 11]