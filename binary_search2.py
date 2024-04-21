def search2a(lst: list, item):
    mid = len(lst) // 2
    if len(lst) <= 1:
        # fill in "base case" (does _not_ include search2())
        if len(lst) == 0:
            return False
        elif lst[0] == item:
            return True
        else:
            return False
    else:
        # fill in recursive case (must involve search2())
        if lst[mid] > item:
            return search2(lst[:mid], item)
        elif lst[mid] < item:
            return search2(lst[mid+1:], item)
        elif lst[mid] == item:
            return True


def binary_search2(search_lst, search_item):
    search_lst.sort()
    return search2(search_lst, search_item)

# assumption is binary search is sorted

# boolean logic


numbers = [1, 3, 5, 7, 12, 33]
print(binary_search2(numbers, 5))
print(binary_search2(numbers, 33))

numbers = [5, 2, 8, 1, 9, 3, 13]
print(binary_search2(numbers, 9))
print(binary_search2(numbers, 2))

fruits = ["apple", "banana", "orange", "grape"]
print(binary_search2(fruits, "grape"))
print(binary_search2(fruits, "pear"))

empty_lst = []
print(binary_search2(empty_lst, 10))

numbers = [10, 20, 30, 40, 50]
print(binary_search2(numbers, 5))
print(binary_search2(numbers, 20))
print(binary_search2(numbers, 40))
