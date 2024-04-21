def linear_search(searchList, searchTerm):
    # searchList.sort()
    for i in range(len(searchList)):
        if searchList[i] == searchTerm:
            return i
    return False

# desk-check
# https://education.nsw.gov.au/teaching-and-learning/curriculum/tas/tas-curriculum-resources-7-12/tas-11-12-curriculum-resources/hsc-algorithms-and-desk-checking

# action: please try desk-checking the linear_search _without_ the sort.

# examples

numbers = [1, 3, 5, 7, 12, 33]
print(linear_search(numbers, 5))
print(linear_search(numbers, 33))

numbers = [5, 2, 8, 1, 9, 3, 13]
print(linear_search(numbers, 9))
# with and without sort, i is changing
# with: i = 5
# without: i = 4
print(linear_search(numbers, 2))


fruits = ["apple", "banana", "orange", "grape"]
print(linear_search(fruits, "grape"))
print(linear_search(fruits, "pear"))

empty_list = []
print(linear_search(empty_list, 10))

numbers = [10, 20, 30, 40, 50]
print(linear_search(numbers, 5))
print(linear_search(numbers, 20))
print(linear_search(numbers, 40))
