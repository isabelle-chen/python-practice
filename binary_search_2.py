def binary_search(search_list, search_item):
    search_list.sort()

    # loop
    lower = 0
    upper = len(search_list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if search_list[mid] < search_item:
            lower = mid + 1
        elif search_item < search_list[mid]:
            upper = mid - 1
        else:
            return True
    return False

    # recursion
    def search(lower, upper):
        mid = (lower + upper) // 2

        # base case
        if lower > upper:
            return False

        if search_list[mid] < search_item:
            lower = mid + 1
            return search(lower, upper)
        elif search_item < search_list[mid]:
            upper = mid - 1
            return search(lower, upper)
        else:
            return True
            # return mid

    # recursive (meaning function call to ourselves) vs iterative (meaning loops)

    return search(lower=0, upper=len(search_list) - 1)


# def search2(list, item):
#     # fill me in
#     if (condition):
#         # fill in base case
#         pass
#     else:
#         # fill in recursive case
#         pass
#         search2() # once or more


def search2(list, item):
    mid = len(list)//2
    if len(list) <= 1:
        # fill in "base case" (does _not_ include search2())
        if len(list) == 0:
            return False
        elif len(list) == 1:
            if list[0] == item:
                return True
    else:
        # fill in recursive case (must involve search2())
        if list[item] < list[mid]:
            return search2(list[0], list[mid])
        elif list[mid] < list[item]:
            return search2(list[mid], list[-1])
        elif list[mid] == list[item]:
            return True

        #search2() # once or more

def binary_search2(search_list, search_item):
    search_list.sort()
    return search2(search_list, search_item)


# boolean logic

numbers = [1, 3, 5, 7, 12, 33]
print(binary_search(numbers, 5))
print(binary_search(numbers, 33))

numbers = [5, 2, 8, 1, 9, 3, 13]
print(binary_search(numbers, 9))
print(binary_search(numbers, 2))

fruits = ["apple", "banana", "orange", "grape"]
print(binary_search(fruits, "grape"))
print(binary_search(fruits, "pear"))

empty_list = []
print(binary_search(empty_list, 10))

numbers = [10, 20, 30, 40, 50]
print(binary_search(numbers, 5))
print(binary_search(numbers, 20))
print(binary_search(numbers, 40))
