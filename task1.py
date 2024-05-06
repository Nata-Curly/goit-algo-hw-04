import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def timsort(arr):
    arr.sort()


def test_sorting_algorithm(sort_algorithm, arr):
    return timeit.timeit(lambda: sort_algorithm(arr.copy()), number=1)


array_sizes = [10, 100, 1000, 2000, 5000, 10000]

for size in array_sizes:
    arr_random = [random.randint(0, 10000) for _ in range(size)]

    print(f"Array size: {size}")
    print("Merge Sort:", test_sorting_algorithm(merge_sort, arr_random))
    print("Insertion Sort:", test_sorting_algorithm(insertion_sort, arr_random))
    print("Timsort:", test_sorting_algorithm(timsort, arr_random))

    print("-" * 40)
