test_list = [2, 4, 7, 8, 9, 10, 12, 34, 45]


def binary_search(my_list, search_item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = my_list[middle]
        if guess == search_item:
            return middle
        if guess > search_item:
            high = middle - 1
        else:
            low = middle + 1
    return None


print(binary_search(test_list, 7))

print(binary_search(test_list, 34))
