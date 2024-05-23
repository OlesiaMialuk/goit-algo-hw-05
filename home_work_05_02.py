
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        # Якщо значення в середині списку менше за шукане, ігноруємо ліву половину
        if arr[mid] < target:
            low = mid + 1

        # Якщо значення в середині списку більше або рівне шуканому, ігноруємо праву половину
        else:
            high = mid - 1

    # Повертаємо кількість ітерацій та "верхню межу" - найменший елемент, який є більшим або рівним заданому значенню
    upper_bound = arr[low] if low < len(arr) else None
    return iterations, upper_bound

arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
target = 0.5
iterations, upper_bound = binary_search(arr, target)
if upper_bound is not None:
    print(f"Елемент знайдено за {iterations} ітерацій, його верхня межа: {upper_bound}")
else:
    print("Елемент не знайдено у масиві")