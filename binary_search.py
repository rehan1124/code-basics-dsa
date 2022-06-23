"""
### Binary Search ###
Binary search happens in sorted list/array.
We discard half of the elements in list/array by location middle element and then comparing it with item to be searched.
Ex: sample_list = [0, 2, 4, 6, 8, 10]
We need to search 8. On doing liner search, time-complexity will be O(n).
Acc. to Binary Search, we locate middle element (6), middle element (6) < item to be searched (8), discard items to
left of 6 ([0, 2, 4]) and search only in [6, 8, 10]. This way time-complexity is reduced to O(Log n).
"""
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) + " milli-seconds")
        return result

    return wrapper


@time_it
def linear_search(number_list, search_number):
    for i, j in enumerate(number_list):
        if search_number == j:
            return i
    return -1


@time_it
def binary_search(number_list, search_number):
    left_index = 0
    right_index = len(number_list) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_item = number_list[middle_index]
        if middle_item == search_number:
            return middle_index
        if middle_item < search_number:
            left_index = middle_index + 1
        if middle_item > search_number:
            right_index = middle_index - 1

    return -1


def recursive_binary_search(number_list, search_number, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = number_list[mid_index]

    if mid_index > len(number_list):
        return -1

    if search_number == mid_number:
        return mid_index

    if mid_number < search_number:
        left_index = mid_index + 1

    if mid_number > search_number:
        right_index = mid_index - 1

    return recursive_binary_search(number_list, search_number, left_index, right_index)


if __name__ == "__main__":
    # sample_list = [12, 15, 17, 19, 21, 24, 45, 67, 69, 72, 80, 90, 120, 130]
    # find_number = 120

    sample_list = [i for i in range(1000001)]
    find_number = 99999

    linear_search_index = linear_search(sample_list, find_number)
    print(f"Found number {find_number} at index {linear_search_index}")

    binary_search_index = binary_search(sample_list, find_number)
    print(f"Found number {find_number} at index {binary_search_index}")

    recur_binary_search_index = recursive_binary_search(sample_list, find_number, 0, len(sample_list))
    print(f"Found number {find_number} at index {recur_binary_search_index}")
