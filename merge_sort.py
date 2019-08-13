# -*- encoding: utf-8 -*-

import math

def merge_sort(list):
    '''
    Sorts a list using the merge sort algorithm, the steps are the following:
    Divide: divides the list into subarrays by halving each part
    Compare: compares each subarray to its closest neighbour
    Join: joins the list back and sorts again for the subsets
    '''

    if len(list) <= 1:
        return list

    left_split, right_split = split(list)
    left = merge_sort(left_split)
    right = merge_sort(right_split)

    return merge(left, right)

def split(list):
    midpoint = len(list) / 2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right

def merge(a, b):
    sorted = []
    left_index = 0
    right_index = 0

    while left_index < len(a) and right_index < len(b):
        if a[left_index] < b[right_index]:
            sorted.append(a[left_index])
            left_index += 1
        else:
            sorted.append(b[right_index])
            right_index += 1

    # If the left array contains more than 1 element, continue adding those elements
    while left_index < len(a):
        sorted.append(a[left_index])
        left_index += 1

    # If the right array contains more than 1 element, continue adding those elements
    while right_index < len(b):
        sorted.append(b[right_index])
        right_index += 1

    return sorted

def verify_list(list):
    '''
    Verify that a list is correctly sorted recursively
    It checks each pair of elements, then moves to the next pair recursively until it's complete
    '''
    # Check the first 2 elements, delete the first one
    if len(list) <= 1:
        return True
    else:
        return list[0] <= list[1] and verify_list(list[1:])

    # Without recursion
    # last_element = -float('inf')
    # for element in list:
    #     if last_element > element:
    #         return False
    #     last_element = element
    # return True


example_list = [19, 22, 13, 291, 35, 83, 55, 49, 2, 353, 423]
print('Original', example_list)
print('Sorted', merge_sort(example_list))
print('Verify list one', verify_list(example_list))
print('Verify list two', verify_list(merge_sort(example_list)))
