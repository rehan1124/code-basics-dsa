"""
### Quick sort ###
Follows divide and conquer
Partitioning: Adding pivot element at its right position
--- 2 types of partition schemes ---
1) Hoare partition
2) Lomuto partition
"""


def quick_sorting(sample_list):
    print(f"Got list: {sample_list}")
    smaller, equal, larger = [], [], []
    if len(sample_list) < 2:
        return sample_list

    pivot = sample_list[-1]
    print(f"Pivot element >>> {pivot}")

    for item in sample_list:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            larger.append(item)

    print(f"Processing: {smaller}, {equal}, {larger}")
    return quick_sorting(smaller) + quick_sorting(equal) + quick_sorting(larger)


if __name__ == "__main__":
    given_list = [11, 9, 29, 7, 2, 15, 28]
    qs = quick_sorting(given_list)
    print(f"After quick-sorting: {qs}")  # [2, 7, 9, 11, 15, 28, 29]
