# First, we need a function definition: MergeSort should take
# as input_lst one list.

# Then, what does it do? mergesort should recursively
# run mergesort on the left and right sides of lst until
# it's given a list only one item. So, if lst has only
# one item, we should just return that one-item list.

# Otherwise, we should call mergesort separately on the
    # left and right sides. Since each successive call to
    # mergesort sends half as many items, we're guaranteed
    # to eventually send it a list with only one item, at
    # which point we'll stop calling mergesort again.

# Floor division on the length of the list will
        # find us the index of the middle value.

# lst[:midpoint] will get the left side of the
# list based on list slicing syntax. So, we want
# to sort the left side of the list alone and
# assign the result to the new smaller list left.

# And same for the right side.

# So, left and right now hold sorted lists of
        # each half of the original list. They might
        # each have only one item, or they could each
        # have several items.

        # Now we want to compare the first items in each
        # list one-by-one, adding the smaller to our new
        # result list until one list is completely empty.

# If the first number in left is lower, add
            # it to the new list and remove it from left

# Otherwise, add the first number from right
# to the new list and remove it from right


# When the while loop above is done, it means
        # one of the two lists is empty. Because both
        # lists were sorted, we can now add the remainder
        # of each list to the new list. The empty list
        # will have no items to add, and the non-empty
        # list will add its items in order.


# newlist is now the sorted version of lst! So,
# we can return it. If this was a recursive call
# to mergesort, then this sends a sorted half-
# list up the ladder. If this was the original
# call, then this is the final sorted list.

def mergesort(input_lst: list):
    new_list = []

    if len(input_lst) <= 1:
        return input_lst
    else:
        midpoint = len(input_lst) // 2
        left = mergesort(input_lst[:midpoint])
        right = mergesort(input_lst[midpoint:])

        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                new_list.append(left[0])
                del left[0]
            else:
                new_list.append(right[0])
                del right[0]

        new_list.extend(left)
        new_list.extend(right)

        return new_list

# Let's try it out!
print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))