
def bubble_sort(L):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(L) - 1):
        made_swap = False
        for j in range(len(L)-1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                made_swap = True
        if not made_swap:
            break
    return L

print bubble_sort([3, 5, 7, 2, 4, 1])


def merge_lists(lst1, lst2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    result_list = []

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            result_list.append(lst1.pop(0))
        else:
            result_list.append(lst2.pop(0))

    return result_list

print merge_lists([1, 3, 9], [4, 7, 11])


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) < 2:
        return lst

    mid = int(len(lst) / 2)
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return merge_lists(lst1, lst2)

print merge_sort([6, 2, 3, 9, 0, 1])


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
