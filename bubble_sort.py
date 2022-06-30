"""
### Bubble Sort ###
Time complexity is O(n2)
Space complexity is O(n)
"""


def bubble_sort(sort_list):
    size = len(sort_list)

    for i in range(size - 1):
        is_swapped = False
        print(f"##### i -> {i} #####")
        for j in range(size - 1 - i):
            print(f"----- Change j to {j} -----")
            print(f"Check {sort_list[j]} > {sort_list[j + 1]}")
            print(f"Initial state: {sort_list}")
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
                print(f"After sorting: {sort_list}")
                is_swapped = True
        if not is_swapped:
            break

    return sort_list


if __name__ == "__main__":
    sample_list = [5, 9, 2, 1, 67, 34, 88, 34]
    # sample_list = [1, 2, 4]
    bs = bubble_sort(sample_list)
    print(f"Bubble sorted list: {bs}")  # Bubble sorted list: [1, 2, 5, 9, 34, 34, 67, 88]
