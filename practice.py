# def bubble_sort(L):
#     """Returns a sorted list using a optimized bubble sort algorithm
#     i.e. using a variable to track if there hasn't been a swap."""

#     for i in range(len(L)-1):
#         made_swap = False
#         for j in range(len(L)-1 -i):
#             if L[j]>L[j+1]:
#                 L[j], L[j+1]=L[j+1], L[j]
#                 made_swap=True
#         if not made_swap:
#             break
#     return L

# print bubble_sort([3, 5, 7, 2, 4, 1])
# # >>> bubble_sort([3, 5, 7, 2, 4, 1])
# #         [1, 2, 3, 4, 5, 7]

# def merge_lists(lst1, lst2):
#     """Given two sorted lists of integers, returns a single sorted list
#     containing all integers in the input lists.

#     >>> merge_lists([1, 3, 9], [4, 7, 11])
#     [1, 3, 4, 7, 9, 11]
#     """

#     result_list = []

#     while len(lst1) > 0 or len(lst2) > 0:
#         if lst1 == []:
#             result_list.append(lst2.pop(0))
#         elif lst2 == []:
#             result_list.append(lst1.pop(0))
#         elif lst1[0] < lst2[0]:
#             result_list.append(lst1.pop(0))
#         else:
#             result_list.append(lst2.pop(0))

#     return result_list

# print merge_lists([1, 3, 9], [4, 7, 11])



# merge_lists([1,3,9], [4,7,11])




# def merge_sort(lst):
#     """
#     Given a list, returns a sorted version of that list.

#     Finish the merge sort algorithm by writing another function that takes in a
#     single unsorted list of integers and uses recursion and the 'merge_lists'
#     function you already wrote to return a new sorted list containing all
#     integers from the input list. In other words, the new function should sort
#     a list using merge_lists and recursion.

#     >>> merge_sort([6, 2, 3, 9, 0, 1])
#     [0, 1, 2, 3, 6, 9]
#     """
#     if len(lst) < 2:
#         return lst

#     mid = int(len(lst) / 2)
#     lst1 = merge_sort(lst[:mid])
#     lst2 = merge_sort(lst[mid:])


#     return merge_lists(lst1,lst2)

# print merge_sort([6, 2, 3, 9, 0, 1])

# my_list = [1, 2, 3, 4]

# def list_length(my_list):
#     """Returns the length of list recursively.
#         >>> list_length([1, 2, 3, 4])
#         4

#     """
#     if not my_list:
#         return 0

#     return 1 + list_length(my_list[1:])

# print list_length(my_list)

# my_list = [1,2,3]

# def print_item(my_list, i=0):
#     """Prints each item in a list recursively.

#         >>> print_item([1, 2, 3])
#         1
#         2
#         3

#     """
#     if len(my_list) == i:
#         return

#     print item,
#     print_item(i + 1)




# print_item(my_list)

# def print_all_tree_data(node):
#     """Prints all of the nodes in a tree.


#         >>> class Node(object):
#         ...     def __init__(self, data):
#         ...             self.data=data
#         ...             self.children = []
#         ...     def add_child(self, obj):
#         ...             self.children.append(obj)
#         ...
#         >>> one = Node(1)
#         >>> two = Node(2)
#         >>> three = Node(3)
#         >>> one.add_child(two)
#         >>> one.add_child(three)
#         >>> print_all_tree_data(one)
#         1
#         2
#         3"""

#     print node.data
#     for child in node.children:
#         print_all_tree_data(child)


# class Node(object):
#     def __init__(self, data):
#         self.data=data
#         self.children = []
#     def add_child(self, obj):
#         self.children.append(obj)

# one = Node(1)
# two = Node(2)
# three = Node(3)
# one.add_child(two)
# one.add_child(three)
# print_all_tree_data(one)


def num_nodes(node):
    """Counts the number of nodes.
        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """
    num = 1

    for node in node.children:
        num = num + num_nodes(node)

    return num


class Node(object):

    def __init__(self, data):

        self.data = data
        self.children = []

    def add_child(self, obj):

        self.children.append(obj)

one = Node(1)
two = Node(2)
three = Node(3)
one.add_child(two)
one.add_child(three)
print num_nodes(one)
# four = Node(4)
# five = Node(5)
# two.add_child(four)
# two.add_child(five)
# print num_nodes(one)
# six = Node(6)
# three.add_child(six)
# print num_nodes(one)
